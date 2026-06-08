---
layout:     post
title:      "Distributed AI Inference Best Practices & Gotchas"
subtitle:   ""
description: "A deep dive into 5D parallelism, P/D disaggregation, KV cache optimization, speculative decoding, and deployment blueprints for distributed AI inference at scale."
date:       2026-06-05
author:     "Yuan Tang"
tags:
    - Open Source
    - Kubernetes
    - Artificial Intelligence
    - Machine Learning
    - KServe
---

*Originally posted on [Medium](https://medium.com/enterpriseai/distributed-ai-inference-best-practices-gotchas-911102c9a2ff)*.

***Authors:** Fatih Nar, Yuchen Fama, Greg Pereira, Yuan Tang*

***Reviewers**: Taneem Ibrahim, Robert Shaw, Ron Haberman, Anish Asthana*

## **1\. Introduction**

In our [Part-I article](https://developers.redhat.com/articles/2025/10/30/why-vllm-best-choice-ai-inference-today), we evaluated vLLM alongside other state-of-the-art model-serving options and established it as the runtime backbone for enterprise AI inference. Choosing the runtime is foundational, but it does not by itself determine how the service is deployed, scaled, operated and maintained. 

In Part-II (this article) we architect the serving blueprint by mapping a model's needs, a hardware budget, and service-level objectives onto the deployment manifest(s) that fit the actual workload. No single blueprint fits every case, because the workload is shaped by the business behind it:

* how many requests arrive at once,  
* how long the prompts and contexts run,  
* the subject-matter domain, and  
* how much reasoning each request demands.

We map business needs to a few short-listed major KPIs: time to first token (TTFT), time per output token (TPOT, or inter-token latency), throughput in requests-per-second and tokens-per-second, GPU utilization, and Key-Value (KV) cache hit rate. These trade against each other constantly, so most deployment decisions are about which trade you can tolerate for which workload, and for what business benefit.

![][image2]

Figure-1 Distributed Inference Decision Framework

Three key things have developed in the ecosystem since Part-I was published:

* The llm-d project’s acceptance into the CNCF Sandbox gives it a clearer open-governance path and makes it easier to evaluate in environments where vendor neutrality, community stewardship, and long-term ecosystem alignment matter.

* KV-cache management has become one of the most active areas of innovation in distributed inference. Projects such as NIXL, LMCache, and Mooncake are competing and converging around different approaches to KV-cache transfer, reuse, and offload. For platform teams, this means cache architecture is now a first-class design decision: it affects latency, network requirements, failure handling, observability, hardware affinity, and the sizing of prefill and decode pools.

* Speculative decoding is moving from research technique to practical optimization path. EAGLE 3.1, a collaboration between the EAGLE team, the vLLM team, and TorchSpec, landed in late May 2026 with materially better long-context acceptance length than EAGLE-3. It makes speculative decoding more relevant for long-document workloads that were previously borderline, while leaving the core engineering question intact: whether the acceptance rate, memory overhead, batching behavior, and operational complexity justify enabling it for a given deployment.

**Note:** The high-value AI models we use for our examples throughout the article (based on our industry-specific [assessments](https://open-experiments.github.io/Telco-AIX/)) are Alibaba's Qwen3.5 and Qwen3.6 families, in both dense (Qwen3.6-27B) and mixture-of-experts (Qwen3.5-35B-A3B and Qwen3.5-397B-A17B) variants. These models are useful anchors because they span a realistic enterprise serving spectrum: smaller dense models for general-purpose latency-sensitive workloads, mid-sized MoE models for cost-efficient throughput, and larger MoE models for high-capability workloads that stress routing, memory, and distributed execution.


## **2\. Prefill/Decode: Two phases, Two KPIs**

LLM inference is two workloads pretending to be one.

* **Prefill** processes the input prompt and populates the KV cache. Because the prompt tokens can be processed in parallel, this phase is dominated by dense matrix operations and tends to be compute-bound. It is the primary driver of time to first token (TTFT), especially for long prompts and retrieval-augmented generation workloads.

* **Decode** generates the response token by token, repeatedly attending over the accumulated KV cache as each new token is produced. This phase tends to be memory-bandwidth-bound: it stresses HBM capacity and bandwidth more than raw compute, and it is the primary driver of time per output token (TPOT), also called inter-token latency.

![][image5]

Figure-2 Prefill vs Decode

The two phases interfere whenever they share a GPU, because the batching strategy that helps one hurts the other. Aggressive batching accumulates enough prompt tokens to use GPU compute efficiently, but a large prefill batch can occupy the worker long enough to delay the decode steps queued behind it, raising TPOT and making streaming feel uneven. Prioritizing decode is the opposite failure: it protects inter-token latency but leaves prefill under-batched, wasting compute and raising the cost of long prompts. The business-level symptoms follow directly: a fleet tuned only for decode feels responsive in chat while burning capacity on prefill-heavy work, and a fleet tuned only for prefill posts healthy aggregate tokens-per-second while making interactive users wait too long for the first token. This prefill/decode split is a foundational lens for much of what follows, starting with disaggregation in Section 4\.

That leads to an architectural fork. The first path is to run prefill and decode together on the same homogeneous workers and let the scheduler arbitrate between them. This is the default shape for single-GPU vLLM deployments, and it remains the right answer for many small and medium-sized fleets because it is simpler to operate and avoids KV-cache transfer overhead. The second is to split them across heterogeneous pools and route each request through both. The threshold for that split is not a model size or a token count, but a measurable imbalance between the two phases, one large enough that the savings from right-sizing each pool exceed the cost of moving the KV cache between them.

| Phase | Bound by | Scales with | Right-sized hardware | KPI it drives |
| :---- | :---- | :---- | :---- | :---- |
| Prefill | Compute (FLOPs) | Prompt length | H100/H200, MI300X, B100/B200/B300 | TTFT |
| Decode | Memory bandwidth | Concurrent active sessions | A100, L40S, MI300, older H100 | TPOT |

Table-1 P/D Attributes

## **3\. The 5D Parallelism** 

Modern LLM serving spans a five-dimensional design space :

* Tensor parallelism (TP),   
* Pipeline parallelism (PP),   
* Expert parallelism (EP),   
* Data parallelism (DP), and   
* Context (sequence) parallelism (CP) which often splits into Prefill Context Parallel (PCP) and Decode Context Parallel (DCP).

While Part-I introduced the first four, CP has become a first-class fifth dimension because Qwen3.5's native 262k-token context makes it unavoidable for any serious long-context deployment.

![][image4]

Figure-3 5D Parallelism 

**Tensor parallelism (TP)** splits each weight matrix across GPUs and runs an all-reduce per layer. This is latency-sensitive within a node and communication-heavy across nodes, so NVLink and NVSwitch are effectively the budget that decides how far TP can scale before the all-reduce dominates. For dense models, the general best practice is to try the quantized version first, then use the minimum TP that fits the model with adequate KV headroom, then scale out with DP. The exception is a stringent single-request TTFT SLO, which can justify higher TP. For MoE models, where DP ranks coordinate on the expert layers, the TP/DP split differs because it determines how the experts are distributed. 

**Pipeline parallelism (PP)** splits the model by layer ranges and passes activations between stages. Because it exchanges activation tensors point-to-point at the stage boundaries rather than running an all-reduce every layer, it is far more tolerant of limited inter-node bandwidth than TP, and it can run over Ethernet-class fabrics where cross-node TP would stall. However that tolerance is relative, not absolute: the handoffs still sit on the critical path, the activation volume grows with batch size, sequence length, and hidden dimension, and any added link latency widens the pipeline bubbles that form when one stage waits on its predecessor. Micro-batching exists to hide those bubbles by keeping every stage fed. All of this makes PP useful when a model is too large to fit one node and the inter-node fabric isn't fast enough for cross-node TP, but it is a last resort, not a default for large models: quantize first, then try EP+DP on one node, and reach for PP only when the weights genuinely don't fit.

**Expert parallelism (EP)** distributes the experts of an MoE model across GPUs. Because each token is routed only to its assigned expert subset, traffic becomes asymmetric and bursty, and one or two popular experts can become tail-latency anchors for the whole fleet under skewed routing. Expert Parallel Load Balancing (EPLB) can replicate hot experts and rebalance routing dynamically, but it is not free: under stable routing patterns the rebalancing overhead may exceed the benefit, so enable EPLB when monitoring confirms persistent imbalance rather than as a blanket default. EP has two further costs. 

* Couples DP ranks that would otherwise be independent, because the expert layers synchronize on every forward pass even when some ranks have fewer requests.   
* Requires all-to-all traffic that scales with the number of active experts and the batch size.

**Data parallelism (DP)** runs full model replicas behind a load balancer for linear throughput scaling with no model-sharding complexity. It is a common starting point when the model fits one node and the bottleneck is concurrent request volume; KServe's ReplicaSet-based serving handles this case directly. DP alone does not set the ceiling, though: the parallelism configuration and routing strategy determine the real performance limit. Common pitfalls:

* stacking more DP replicas without checking for API-server bottlenecks,  
* ignoring KV-cache hit rate and MoE synchronization overhead, and  
* underestimating multi-node network costs.

**Context parallelism** **(CP)** shards the sequence (context) dimension across GPUs, so that a single request's context no longer has to fit, or be computed, on one device. Long context stresses prefill and decode in different ways, and the two phases carry different SLOs, so CP is applied separately to each as PCP and DCP.

* **Prefill context parallel (PCP)** targets TTFT. During prefill, attention cost grows with the square of the prompt length, so a long prompt can dominate time to first token. PCP partitions the sequence across devices and lets each one compute attention over its own chunk in parallel, which splits the prefill compute across GPUs and brings TTFT down. The cost is hardware: PCP expands the world size and runs in its own communication domain, so the device count becomes TP × PCP. Reach for it when prefill compute is what dominates TTFT and the GPU budget allows.  
* **Decode context parallel (DCP)** targets throughput. During decode the bottleneck is KV-cache capacity: the more KV you can hold, the larger the batch, and the higher the throughput. DCP shards the KV cache along the sequence dimension across the GPUs already in the tensor-parallel group, reusing the TP communication domain, so it needs no extra devices. It is most valuable for models with few KV heads, such as Qwen3.5: under plain TP, when there are fewer KV heads than TP ranks, the KV cache is replicated across ranks and wastes HBM, and DCP removes that duplication and hands the freed memory back to the batch. Decode context parallel is supported in vLLM for both MLA and GQA models, and some attention backends can combine it with multi-token prediction (MTP) to accelerate decoding further.

Because DCP costs no additional GPUs and directly reduces KV duplication, it is the one most deployments should reach first. PCP is the heavier tool, added when a long prefill is the thing blowing the TTFT budget.

| Model | Hardware/Precision | Suggested layout | Notes |
| :---- | :---- | :---- | :---- |
| Qwen3.6-27B (dense) | 1×H100, FP8 | TP=1 | \~27 GB weights; single-GPU baseline |
| Qwen3.6-27B (dense) | 8×H100, FP8 | DP=8 | TP=1 per replica |
| Qwen3.5-35B-A3B (MoE) | 8×H100, FP8 | DP=8,  \--enable-expert-parallel | EP=8; experts sharded |
| Qwen3.5-35B-A3B (MoE) | 8×H100, BF16 | TP=2, DP=4,  \--enable-expert-parallel | \~70 GB weights → TP=2 to fit; EP=8 |
| Qwen3.5-397B-A17B (MoE) | 16×H100 (2 nodes), FP8 | PP=2, EP=8,  \--enable-expert-parallel | \~397 GB weights; layers split across the two nodes, experts split within each |
| Any Qwen3.5 ≥128k decode | \+ DCP (on top of above) | \--decode-context-parallel-size 2 | Shards KV on existing TP GPUs; no new devices |
| Any Qwen3.5 ≥128k prefill | \+ PCP (on top of above) | \--prefill-context-parallel-size 2 | Adds GPUs (TP × PCP) |

Table-2 P/D AI Model vs Hardware vs Parallelism Options

**Note:** vLLM computes EP \= TP × DP per pipeline stage, so EP= in the table is for convenience. The optimal configuration of different parallelism combinations depends on the model architecture and hardware. Expert Parallelism can be latency-optimal for models like Qwen 3 with limited Key-Value heads, whereas Data Parallelism maximizes throughput but may introduce latency issues due to dispatch bubbles during the prefill and decode stages.

## **4\. P/D Disaggregation as a Deployment Pattern**

Part-I described disaggregation as a feature of llm-d, but in practice it is a deployment topology (the most consequential one we cover here), and we need to reason about it as such rather than check it off as a capability.

![][image6]

Figure-4 Prefill/Decode 

**When to disaggregate.** The decision rule is neither "always" nor "for big models," but determined from measurable observations within the system. Profile a baseline single-pool deployment and measure the ratio of prefill GPU-seconds to decode GPU-seconds on your real traffic, then compare it to the ratio of decode-optimized to prefill-optimized GPU cost in your environment. If your traffic is prefill-heavy while you are paying for decode-class hardware (because decode dominates wall-clock), or vice versa, the gap between those two ratios is the upside available from disaggregation. The decision tends to pay off for long-prompt RAG with short answers (prefill-heavy), for high-concurrency chat with short prompts and long answers (decode-heavy), and for any fleet large enough that the $/Mtoken reduction justifies the operational complexity. In our benchmarks that reduction runs 25–40% on chat- and RAG-shaped traffic, consistent with published disaggregation results: [Splitwise](https://arxiv.org/abs/2311.18677) reports about 20% lower cost at 1.4× throughput, and [DistServe](https://arxiv.org/abs/2401.09670) up to 7.4× higher goodput. It tends not to pay off for single-node deployments where the network hop between prefill and decode workers would exceed the savings, nor for any fleet small enough that two pools of one are worse than one pool of two.

**Sizing the two pools.** Prefill workers scale with the arrival rate of new prompts and with prompt-length distribution, while decode workers scale with concurrent active sessions, average token output sizing and target TPOT, and the two scale independently. A useful first cut for a chat workload with mean prompt 800 tokens and mean output 200 tokens at 5,000 concurrent sessions on Qwen3.5-35B-A3B works out to roughly one H100 of prefill capacity per \~30 requests/second of arrival rate, and roughly one decode GPU (L40S-class) per \~150 concurrent sessions, in our lab measurements. These numbers move with model and quantization, but the ratio (typically 1:3 to 1:5 prefill to decode workers for chat) is broadly stable across the workloads we have benchmarked.

**KV-transfer connectors and the data path.** Once the pools are split, the KV cache produced by prefill must reach decode workers, and vLLM exposes a KVConnector interface with three production-relevant implementations.

| Connector | Best for | Transport | Notes |
| :---- | :---- | :---- | :---- |
| NixlConnector | Single-cluster, RDMA/NVLink available | NVIDIA NIXL over UCX | Default for high-performance PD; metadata server is a startup SPOF |
| LMCacheConnector | Cross-instance cache sharing, HBM→DRAM→NVMe tiering | NIXL under the hood, plus offload backends | Adds tiered KV cache \+ shared prefix index ([LMCache, arXiv:2510.09665](https://arxiv.org/abs/2510.09665)) |
| MooncakeConnector | Cluster-scale shared cache pools | RDMA-native | Best when you want a separate KV-cache cluster that many vLLM instances pull from |
| MooncakeStoreConnector | Tiered cache offloading through use of a distributed master store | Cache offloading | Offload tier behind MooncakeConnector; KV lands in a distributed master store rather than peer HBM |

Table-3 KV-Cache Connectors

Treat the KV-transfer fabric the way you would treat any other production data path: measure end-to-end latency including queue time, alert on tail latency rather than mean, and verify RDMA driver health on every node, because NIXL's asynchronous send/receive is the right primitive for production only if prefill workers are never made to block on decode-side acknowledgement.

**The disaggregated KV cache pool.** We find the most useful framing is to stop thinking of the cluster's KV cache as per-worker memory plus a transfer protocol, and start treating it as a cluster-wide resource with its own scheduling concerns. [LMCache](https://arxiv.org/abs/2510.09665) makes this explicit by tiering across HBM, DRAM, and NVMe and exposing a global prefix index, so that when two requests share a prefix (a system prompt, a few-shot prefix, the first thousand tokens of a contract), they share KV blocks no matter which instance generated them.

**The llm-d scheduler.** Cache-aware routing is what turns disaggregation from a feature into a working pattern, because instead of round-robin across decode workers, llm-d routes a request to the worker that already has the warmest KV state for the request's prefix. [Published llm-d benchmarks](https://llm-d.ai/blog/llm-d-v0.5-sustaining-performance-at-scale) report up to 57× faster TTFT and 2× throughput against round-robin routing under high prefix reuse (8 pods / 16×H100). Our internal measurements are more conservative, and illustrative rather than guaranteed: a roughly 25% improvement on defaults, 2–3× tokens-per-second-per-GPU when paired with prefix-cache-hit routing, and 3–5× cost-per-token reduction on chat-shaped workloads where prefix reuse is high. Numbers in any given production deployment will be lower than these lab-style figures, though the direction is reliable across every workload we have measured.

**Hybrid GPU-CPU prefill.** A forward-looking pattern is emerging on Grace Hopper and Vera Rubin superchips, where the CPU side of the superchip handles parts of the prefill (notably embedding lookup and some attention prep) while the GPU handles the matmul-heavy portions. It is not yet a first-line recommendation for production, but it is worth designing the deployment with the prefill pool as a separately scheduled component, so that the worker type can change as the hardware matures without re-architecting.

**Failure modes that bite in production.** The NIXL metadata server is a single point of failure on startup, so run two behind a TCP load balancer and verify failover before the first canary. Decode workers that fall behind the KV transfer become tail-latency anchors for the whole fleet, which is why admission control at the gateway is more useful than retrying after the fact. And canary rollouts for disaggregated fleets should change one pool at a time, with rollback gates on both TTFT and TPOT, so that a regression in either KPI is caught before it spreads.

## **5\. KV Cache: Tiering, Sharing, Squeezing**

[PagedAttention](https://arxiv.org/abs/2309.06180) solved the fragmentation problem inside a single GPU, but the next set of problems lives across GPUs and across the cluster, and they need different tools.

![][image8]

Figure-5 KV-Cache

**Tiered hierarchy.** Section 4 introduced LMCache's HBM→DRAM→NVMe tiering as a cluster-wide resource; the question here is when to turn it on. Most enterprise workloads have a long tail of cold prefixes that fit in DRAM or NVMe but not in HBM, and the decision rule is simple: if your prefix-cache hit rate would be substantially higher with a 10× larger cache than you can afford in HBM, then tiering pays for itself.

**KV reuse vs prefix sharing.** These two are often conflated, but they are different concerns with different configuration knobs. Prefix sharing means that two requests starting with the same tokens share the cache, while KV reuse means that the same request's KV is retained across turns of a multi-turn session. Multi-tenant chat platforms benefit from both, because shared system prompts give one and conversation history gives the other. Prefix sharing is therefore a routing concern (send the new request to the worker that has the warm prefix), while reuse is a session-affinity concern that keeps the same session pinned to the same decode worker.

**Quantization.** [FP8 KV cache](https://vllm.ai/blog/2026-04-22-fp8-kvcache) halves the memory footprint with a measurable but usually acceptable quality cost on most enterprise tasks, while FP4 KV is more aggressive and currently best deployed only on workloads where you can afford an evaluation pass against your own data. Red Hat's [LLM Compressor](https://github.com/vllm-project/llm-compressor) produces quantized variants of the Qwen models and validates them against your own eval set rather than a generic benchmark.

**Decode kernels.** vLLM's decode path is fast in 2026 not because of one optimization but because of a family of them, with [FlashMLA](https://github.com/deepseek-ai/FlashMLA) (DeepSeek), [ThunderMLA](https://hazyresearch.stanford.edu/blog/2025-03-04-thundermla) (Stanford), and PyTorch's FlexAttention decode path all contributing. Platform teams rarely tune these kernels directly, but knowing which one your vLLM build is using helps when investigating an unexpected decode regression after a version upgrade. At fleet scale the harder problem is provenance and consistency: every prefill, decode, and draft-model replica must load identical, pinned kernel binaries, which is why a production runtime ships them build-from-source and SBOM-covered in the image rather than pulling them from a public registry at first request. We cover that kernel supply-chain trade-off, and the GPU Kernel Manager (GKM) bridge for heterogeneous fleets, in [What GPU kernels mean for your distributed inference](https://developers.redhat.com/articles/2026/05/20/what-gpu-kernels-mean-your-distributed-inference).

**PagedAttention vs Radix-Attention.** [SGLang's RadixAttention](https://arxiv.org/abs/2312.07104) takes a different architectural bet by organizing the cache as a prefix tree and letting the structure of conversation guide eviction, whereas PagedAttention treats the cache like virtual memory pages, and reasonable engineers disagree on the trade-off: Radix tends to win on workloads with deep, branching prefix trees (agent workflows, structured prompting), while PagedAttention tends to win on workloads with high variance in sequence length and irregular prefix patterns. vLLM has stayed with PagedAttention because the engine is general-purpose and the page-table abstraction generalizes more cleanly to disaggregation, where the unit of transfer is naturally a page.


## **6\. Speculative Decoding** 

Speculative decoding generates several candidate tokens at once with a cheaper draft path, then verifies them with the target model, so that when the drafts are accepted the model emits several tokens per forward pass. The families of technique that vLLM supports today are worth distinguishing, because their cost profiles are very different.

![][image9]

Figure-6 Speculative Decoding

**Two-model, draft-based (EAGLE family).** A small draft model proposes tokens that the target then verifies. [EAGLE-3](https://arxiv.org/abs/2503.01840) has been reported to reach up to \~6× speedups on dense models, while [EAGLE 3.1](https://vllm.ai/blog/2026-05-26-eagle-3-1) (May 2026\) extends that gain materially into long-context regimes with up to 2× longer acceptance length than EAGLE-3, making it a strong starting choice for dense Qwen3.6 workloads.

**Single-model self-speculative.** The model drafts and verifies itself, typically by using a subset of its own layers as the draft, which gives a lower setup cost (there is no separate draft model to train or host) at the price of a more variable acceptance rate that depends on the workload.

**Multi-token decoding ([Medusa](https://arxiv.org/abs/2401.10774) heads).** Adding multiple output heads to the target model lets it predict several tokens per pass, and although the engineering cost is roughly half that of EAGLE-3 to deploy, the acceptance rates are correspondingly more modest, at around 0.55–0.70.

**Interleaved decode and constrained-decoding interactions.** Less a technique than a scheduling choice, modern vLLM interleaves spec-decoded sessions with normal decode steps to keep batches full. There is one important caveat: when the workload uses constrained decoding (JSON mode, tool calls with grammars), the acceptance rate of speculative decoding often collapses because the constraint mask invalidates speculative tokens, so measure before assuming spec decoding helps in tool-calling traffic.

**Multi-token prediction (MTP).** Some models, notably [DeepSeek-V3](https://arxiv.org/abs/2412.19437), ship with MTP heads trained jointly with the main model, and acceptance rates exceed 80% out of the box. This makes MTP the natural choice for any model that ships MTP-trained, but it cannot be bolted on to models that don't without re-training.

| Workload | Anchor model | Recommended | Why |
| :---- | :---- | :---- | :---- |
| Short conversational, dense | Qwen3.6-27B | EAGLE 3.1 | Best accept-rate/cost ratio, current generation |
| Long-context (\>64k) | Qwen3.5 dense or MoE | EAGLE 3.1 | Long-context acceptance is the headline improvement |
| MoE flagship | Qwen3.5-397B-A17B | Native MTP if trained; else EAGLE-3 | Active-param shape favors MTP-style heads |
| Code completion | Qwen3.6 dense | n-gram / prompt-lookup | Repetitive code structure makes hit rate high; no draft to host |
| Strict memory budget | any | n-gram | No draft model to host on decode GPU |
| Heavy tool-calling traffic | any | Disable or test | Constrained decoding interaction is severe |

Table-4 Speculative Decoding Options vs Workloads

**Note:** The draft model occupies decode-worker HBM and adds verification overhead, so on already-saturated, large-batch decode fleets the win from spec decoding shrinks, because the batch is already amortizing the kernel launch. At the extreme it can become a net loss, so the clearest wins are at low-to-moderate concurrency, where each forward pass is underutilized.

## **7\. Deployment Blueprints by Traffic Shape**

The technique sections above are the tools; this section shows how they assemble into deployments. Each blueprint follows the same structure (workload signature, KPI priority, topology, the vLLM and llm-d mechanisms it leans on, and a note on cost shape), and should be read as a starting point rather than a prescription.

![][image1]

Figure-7 Deployment Blueprints by Traffic 

### **7.1 High-concurrency conversational chat and copilots**

**Signature.** Thousands of concurrent users, prompts in the low hundreds of tokens, outputs of similar length, high prefix reuse from system prompts and few-shot exemplars, and TPOT-dominated SLOs.

**Topology.** The deployment is PD-disaggregated, with a small prefill pool on H100/H200-class hardware and a large decode pool on cost-optimized GPUs (L40S, older H100s, MI300), where cache-aware routing via the llm-d scheduler pins each session to the decode worker holding its warm KV. EAGLE 3.1 runs on the decode workers, and LMCache offloads from HBM to pinned DRAM (and to NVMe for the longest-tail conversations) so that the decode pool's effective cache becomes several times larger than its HBM. On the prefill side, chunked prefill (stall-free scheduling) prevents a long prompt from blocking the short ones queued behind it. At the front door, prompt compression on system prompts, debouncing and request coalescing for chatty UIs, and output token caps protect the fleet from runaway generation. The cost shape is decode-dominated, so right-sizing the decode pool is where most of the $/Mtoken savings live.

### **7.2 Long-context RAG and code analysis**

**Signature.** Lower concurrency than chat, prompts of 32k–256k tokens, outputs in the hundreds, and TTFT-dominated SLOs, because users are waiting for the first useful token of an answer over a long document.

**Topology.** TP within the node and PCP across GPUs for the prefill phase, so the O(n²) attention work is split rather than left to blow HBM on one device. The decode pool stays small; this workload is bound more by prompt length than by concurrency.

Two things buy back TTFT here, and chunked prefill is not one of them. PCP amortizes the prefill compute across devices; prefix caching skips it outright when the document has been seen before. Chunked prefill, on by default in vLLM V1, earns its keep elsewhere: it keeps one long prefill from starving the decode steps of every other request sharing the GPU. On the long prompt itself it adds a little overhead, and prefix caching becomes the whole game: the warm prefix lives in a shared cache pool any decode worker can reach, so the second pass over a contract never re-prefills it.

The cost shape is prefill-dominated, so the biggest lever on $/Mtoken is prefix-cache hit rate: every avoided re-prefill of a long document is a direct saving.

### **7.3 High-throughput batch (summarization, labeling, embeddings pipelines)**

**Signature.** Latency-tolerant, throughput- and dollar-bound, typically running overnight on backlogs.

**Topology.** The pattern is DP-heavy, with as many replicas of the model as fit the budget and each replica running continuous batching maxed out. PD disaggregation tends to buy nothing here, because the wall-clock per request does not matter, so the transfer hop is not worth it. Continuous scheduling, which differs from continuous batching by letting the engine reorder requests to keep batches full even when arrival is bursty, is the right policy. Dynamic quantization can be tuned more aggressively here than in interactive workloads, because a slightly lower output quality is cheaper than a slightly larger GPU footprint. Scale-to-zero between waves via KServe's KEDA integration keeps the cluster economical, and the workload is spot/preemptible-friendly because retries on batch jobs are cheap.

The cost shape is pure $/token: with latency irrelevant, every lever (max batching, aggressive quantization, scale-to-zero, and spot capacity) goes toward driving dollars per million tokens down.


### **7.4 Distributed AI-grid: Model-as-a-Service** 

**Signature.** The most architecturally rich blueprint we cover. A platform team serves multiple tenants and multiple models (Qwen3.6-27B for one product, Qwen3.5-35B-A3B for another, Qwen3.5-397B-A17B reserved for the hard queries) across heterogeneous SLOs and bursty traffic, and the deployment becomes a grid rather than a collection of single-purpose pools.

**Topology.** Each model class lives behind its own llm-d InferencePool, with KServe LLMInferenceService resources tracked in GitOps, and [AI Gateway implementations such as Envoy AI Gateway](https://developers.redhat.com/articles/2026/05/25/route-external-and-local-llms-models-as-a-service) sit at the front door handling tenant authentication, rate limiting, and request classification. A shared LMCache fabric across pools lets system-prompt prefixes be reused across instances of the same model, while KEDA autoscaling runs per request-class rather than per pool, so that a "gold" tenant's bursty traffic can scale its pool aggressively while a "bronze" tenant on the same model sees slower scale-up.

Three mechanisms make this work, and all three were absent or thin in Part-I.

* **Model cascading** routes easy queries to the smallest model that can handle them and escalates to the next size only when needed. A cascade of Qwen3.6-27B → Qwen3.5-35B-A3B → Qwen3.5-397B-A17B, with escalation triggered by an inexpensive confidence signal or by explicit tenant policy, [can cut cluster cost by 40–60%](https://arxiv.org/abs/2603.04445) on workloads where the easy fraction dominates. The cascade itself lives in the gateway rather than inside any single InferencePool, so the routing decision can change without redeploying the model.  
* **SLO-aware admission control** is operationally healthier than queuing requests that will miss their SLO, because the queue itself becomes a tail-latency anchor under load. Gold-tier requests get admitted ahead of silver, silver ahead of bronze, and requests likely to exceed token output limits or hit timeouts are rejected at the gateway with a clear error code rather than allowed to chew through GPU-seconds and then time out anyway.  
* **Adaptive resource scheduling and hotspot prevention** is the layer where llm-d's scheduler does the routing and cluster-level policy does the resource allocation. Adaptive parallelism (TP↔PP↔hybrid switching as traffic patterns shift), dynamic precision (FP8↔FP4 under thermal or load pressure), continuous prewarming of CUDA graphs via traffic-pattern time-series prediction, and MoE expert rebalancing for hot experts are all early-engineering or research today. An AI-grid design that holds up under those changes treats per-tenant SLO classes and telemetry-driven configuration as first-class concerns from the start, so that the static knobs can be swapped for adaptive ones without re-architecting.

The cost shape of this blueprint is the most non-linear of the six. Done well, it can let a platform team serve many tenants at high utilization; done poorly, it becomes a fragmented zoo of single-tenant pools each running at low utilization, and the difference between those two outcomes is almost entirely a matter of cascading, admission control, and shared cache design.

### **7.5 Hybrid Sovereign \-\> Cloud-Burst**

**Signature.** Regulated baseline workload that must run on-premises for data residency, sovereignty, or contractual reasons, with peaks that exceed on-prem capacity and need to burst to a public cloud region without breaking the regulatory posture.

**Topology.** Red Hat OpenShift AI on Red Hat OpenShift provides a single control plane across both environments, with model artifacts in a shared registry and configuration drift managed by GitOps so that the on-prem and burst clusters stay aligned. llm-d's Inference Gateway fronts both clusters, and congestion-aware, topology-aware scheduling routes individual requests to whichever cluster currently has capacity and the warm prefix. The burst cluster runs cold most of the time. What makes its capacity usable when the spike arrives, rather than tens of seconds later, is fast, deterministic warm-up: pre-pulled pinned images and kernels and a minimal standing footprint, with predictive prewarming via time-series traffic forecasting layered on as that capability matures (Section 7.4). The aim is for the CUDA graphs and KV pools to be warm before traffic shifts, not after.

The cost shape is a capex-anchored on-prem baseline plus variable cloud opex paid only during bursts. The economics hold only if the burst cluster stays genuinely cold between peaks, so the lever is a fast warm-up, not standing capacity.

### **7.6 Edge inference on a workstation-class GPU**

**Signature.** A single physical site such as a factory floor, retail location, clinic, branch office, vehicle, or regional data closet, where data residency, latency, or connectivity rule out cloud inference for the baseline workload, and backhaul to a regional cluster (when it exists at all) is expensive or intermittent. Concurrent users are typically in the 1–50 range. Both TTFT and TPOT matter to a human operator, but request volume is low enough that throughput is bounded by a single accelerator rather than by anything in the orchestration layer.

**Topology.** The pattern is a single vLLM instance per accelerator with no llm-d disaggregation, because the prefill-decode transfer hop costs more than it saves below roughly 100 concurrent sessions. KServe handles the serving lifecycle; the OpenShift footprint follows the site: Single Node OpenShift (SNO) for single-node sites, and multi-node OpenShift for regional installations with a handful of cards. GitOps pins the model artifact across the fleet so the same Qwen3.6-27B build runs in every store, clinic, or branch without per-site drift.

**The model fits on 96 GB.** The hybrid architecture of Qwen3.6-27B is unusually edge-friendly because three of every four attention sublayers are Gated DeltaNet (a linear-attention variant whose state does not grow with context length), so only 16 of the 64 layers maintain a per-token KV cache, with 4 KV heads at head\_dim 256\. Per-token KV is therefore roughly 64 KB in FP16 or 32 KB in FP8, several times smaller than a pure-transformer model of comparable parameter count, and after 27 GB of FP8 weights and \~4 GB of working memory the remaining \~65 GB of VRAM holds roughly 2 million tokens of cumulative KV at FP8 KV precision. That budget supports any of: \~50 concurrent sessions at 32k context each, \~15 sessions at 128k each, or \~4 sessions at 512k each (the last with FP4 KV). For larger models the envelope tightens quickly: Qwen3.5-35B-A3B at FP8 leaves around 55 GB for KV (workable for moderate concurrency), while Qwen3.5-397B-A17B will not fit a single card at any production precision because the full expert table must be resident.

**Hardware is substrate, not strategy.** The accelerators at this tier (workstation cards such as the NVIDIA RTX PRO 6000 (96GB) Blackwell, or deskside superchip systems such as DGX Spark and the [Supermicro Super AI Station](https://www.supermicro.com/en/accelerators/nvidia/super-ai-station)) differ mainly in memory bandwidth and capacity, but the software approach is the same across all of them: quantize to fit one accelerator, serve a single vLLM instance, and scale with replicas (DP) before sharding. The one constraint they share is the absence of NVLink-class fabric between boxes, so any multi-box scale-out is a capacity play built on pipeline or expert sharding, not a tensor-parallel throughput play (Section 3). Decode is memory-bandwidth-bound, so the deployment is capex-dominated, and there is no clean $/MToken story until a site outgrows \~100 concurrent sessions and starts to look like a regional cluster.

**Multi-tier pattern.** For edge sites that occasionally see queries too hard for the local model, route them over backhaul to a regional cloud cluster running the Section-7.4 AI-grid, with model cascading at the local gateway keeping the fast path on-device and escalating only when a confidence signal or explicit policy demands the flagship model. p99 latency on local queries stays predictable while the heavier model remains available for the long tail, and the backhaul cost stays bounded because escalations are a fraction of total traffic.


## **8\. Inference Troubleshooting Recipes**

When TTFT or TPOT regress, the first move is not to change anything but to look at the metrics the fleet already emits, because most regressions point at themselves once you know which dial to read. The [vLLM Prometheus endpoint](https://docs.vllm.ai/en/latest/serving/metrics.html) exposes per-request and per-batch metrics (queue time, scheduling delay, prefill duration, decode duration, KV-cache utilization), and the llm-d scheduler emits routing decisions and per-worker queue depths, so the two together answer the first question every time: is the regression at the gateway (routing), in the prefill phase, in the decode phase, or in the KV transfer between them?

For deeper investigation, [Nsight Systems](https://developer.nvidia.com/nsight-systems) captures end-to-end traces and is the right tool when a regression appears to span multiple processes or involves CPU↔GPU coordination, while [Nsight Compute](https://developer.nvidia.com/nsight-compute) drills into a specific kernel when a single operation is the bottleneck.

![][image7]

Figure-8 Troubleshooting Recipes

The recipes that recur most often in production inference work are these:

* Sudden TPOT increase with KV utilization climbing usually means KV-cache fragmentation or over-eager preemption; tune the preemption threshold and verify chunked prefill is enabled if long prompts are starving the short decodes queued behind them.  
* MoE traffic with degraded throughput and one or two experts at much higher queue depth than the others is hot-expert imbalance; enable EPLB, and if the imbalance persists consider expert replication.  
* A disaggregated fleet with TTFT fine but TPOT spikes correlated with prompt arrival means NIXL queue depth is rising and decode workers are blocked waiting for KV transfer; verify RDMA driver health and check that the NIXL metadata server isn't single-pointed.  
* Speculative decoding enabled and throughput unchanged or worse usually means draft-head acceptance rate has decayed; inspect per-request acceptance metrics, because the model or workload may have drifted away from what the draft was trained for.

Roll out changes via canary, gate on both TTFT and TPOT, and never change two scheduler parameters at once, because debugging which one mattered is harder than the original problem.

## **9\. Where to start, where to grow**

A practical sequence for a team standing up vLLM and llm-d on OpenShift AI runs roughly like this.

* Begin on a single node with a single vLLM instance, pick the model and the parallelism layout from the Section-3 table, and baseline TTFT and TPOT on production traffic for at least a week, because the numbers from that baseline are what every later decision will be measured against.  
* Add llm-d when the single-node fleet stops scaling linearly: the signal is that a second replica behind a load balancer produces less than 1.8× the throughput of one, which means round-robin routing is leaving cache hits on the table.  
* Disaggregate only when the measured prefill-to-decode imbalance is large enough to pay for the transfer hop, because disaggregation done prematurely costs more than it saves; layer speculative decoding once concurrency has stabilized, since at low concurrency the wins are largest and at saturated high concurrency they shrink.  
* Reach for the AI-grid blueprint when the platform serves more than one model class to more than one tenant, because the mechanisms (model cascading, SLO classes, shared cache fabric, GitOps-managed pools) earn their complexity at the multi-tenant scale and waste effort below it.

![][image3]

Figure-9 Where to start, where to grow.

The through-line connects every step. Part I chose the runtime; Part II turns that choice into a deployment, adding one mechanism at a time and only when a measurement shows the simpler setup has run out, then re-baselining after each change so the next decision rests on data rather than expectation. Start simple, measure honestly, and identify optimization starting from the workload rather than let the technique catalog decide what comes next.

Each rung of that ladder maps to a layer of the Red Hat stack you can deploy rather than assemble by hand. Red Hat OpenShift provides the Kubernetes substrate; Red Hat OpenShift AI adds the model registry, pipelines, monitoring, and governance; Red Hat AI Inference Server packages a hardened vLLM with pinned kernels and LLM Compressor for quantization; KServe manages the serving lifecycle; and llm-d, now a CNCF Sandbox project, supplies the distributed inference layer for cache-aware routing, disaggregation, and KV-cache-aware scheduling. The blueprints in Section 7 are assembled from these building blocks, and the sequence above is how you adopt them without paying for complexity before the workload calls for it.

To learn more, take a look at these resources:

* [Why vLLM is the best choice for AI inference today](https://developers.redhat.com/articles/2025/10/30/why-vllm-best-choice-ai-inference-today) (Part-I of this series)  
* [llm-d](https://github.com/llm-d/llm-d), the Kubernetes-native distributed inference framework (now a CNCF Sandbox project)  
* [Combining KServe and llm-d for optimized gen-AI inference](https://developers.redhat.com/articles/2026/04/21/kserve-llm-d-optimized-gen-ai-inference)  
* [What GPU kernels mean for your distributed inference](https://developers.redhat.com/articles/2026/05/20/what-gpu-kernels-mean-your-distributed-inference) (the companion piece on kernels and supply-chain discipline)  
* [Red Hat AI Inference Server Technical Deep Dive](https://www.redhat.com/en/blog/red-hat-ai-inference-server-technical-deep-dive)  
* [LLM Compressor](https://github.com/vllm-project/llm-compressor) for producing and validating quantized models  
* vLLM [context-parallel deployment](https://docs.vllm.ai/en/latest/serving/context_parallel_deployment/) and [disaggregated prefilling](https://docs.vllm.ai/en/stable/features/disagg_prefill/) documentation









[image1]: /img/inblog/distributed-ai-inference-best-practices/image1.png
[image2]: /img/inblog/distributed-ai-inference-best-practices/image2.png
[image3]: /img/inblog/distributed-ai-inference-best-practices/image3.png
[image4]: /img/inblog/distributed-ai-inference-best-practices/image4.png
[image5]: /img/inblog/distributed-ai-inference-best-practices/image5.png
[image6]: /img/inblog/distributed-ai-inference-best-practices/image6.png
[image7]: /img/inblog/distributed-ai-inference-best-practices/image7.png
[image8]: /img/inblog/distributed-ai-inference-best-practices/image8.png
[image9]: /img/inblog/distributed-ai-inference-best-practices/image9.png
