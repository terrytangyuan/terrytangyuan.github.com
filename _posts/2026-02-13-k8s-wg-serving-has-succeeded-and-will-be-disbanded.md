---
layout:     post
title:      "Kubernetes Serving Working Group Has Succeeded and Will Be Disbanded"
subtitle:   ""
date:       2026-02-13
author:     "Yuan Tang"
tags:
    - Open Source
    - Kubernetes
    - Artificial Intelligence
    - Machine Learning
---

*Originally posted on [Kubernetes dev mailing list](https://groups.google.com/a/kubernetes.io/g/dev/c/nDjMph1146A/m/z-T7POJQBQAJ)*.

We'd like to announce that Kubernetes WG Serving has succeeded and will be disbanded! Thank you everyone who have participated and contributed to the discussions and initiatives!

# WG Serving Has Succeeded and Will Be Disbanded

The [Kubernetes Working Group Serving](https://github.com/kubernetes/community/tree/1cd8d239089e777d0e2f70d665e7db153f040a80/wg-serving) was created to support development of AI Inference stack on Kubernetes. The goal of this working group is to ensure that the Kubernetes is an orchestration platform of choice for Inference workload. This goal was accomplished and we are disbanding the working group.

The WG Serving formed workstreams to collect requirements from various model servers, hardware providers, and inference vendors. This work resulted in a common understanding of inference workload specifics and trends and laid the foundation for improvements across many SIGs in Kubernetes.

The working group oversaw several key evolutions to the role of load balancing and workloads \- the inference gateway was adopted as a request scheduler, multiple groups have worked to standardize AI gateway functionality, and early inference gateway participants went on to seed agent networking in sig-network. The use cases and problem statements informed the design of [AIBrix](https://github.com/vllm-project/aibrix). And many of the unresolved problems in distributed inference \- especially benchmarking and recommended best practices \- have been picked up by the [llm-d](https://github.com/llm-d/llm-d) project which hybridizes the infrastructure and ML ecosystems and is better able to steer model server co-evolution.

In particular, we believe llm-d and AIBrix represent more appropriate forums for driving requirements to Kubernetes SIGs than this working group. llm-d's goal is to provide well-lit paths for achieving state-of-the-art inference and aims to provide recommendations that can compose into existing inference user platforms.  AIBrix provides a complete platform solution for cost efficient LLM inference.

WG Serving helped with [Kubernetes AI Conformance](https://github.com/cncf/k8s-ai-conformance) requirements and llm-d leveraging multiple components from the profile and making recommendations to end users consistent with Kubernetes direction (Kueue, inference gateway, LWS, DRA, etc.). Widely adopted patterns and solutions are expected to go into the conformance program.

All the efforts currently running inside the WG Serving can be migrated to other WGs or to SIGs directly, requirements for them will be discussed in SIGs and llm-d community. Specifically:

- **Autoscaling** questions \- mostly related to fast bootstrap \- will be either SIG Node or SIG Scheduling.  
- **Multi-host, multi-node** work can continue as part of the SIG Apps (e.g. for LWS project) and DRA requirements discussed in WG Device Management.  
- **Orchestration** will be covered by SIG Scheduling and SIG Node   
- Requirements for **DRA** will be discussed in WG Device Management.

The [Gateway API Inference Extension](https://github.com/kubernetes-sigs/gateway-api-inference-extension) project is already sponsored by SIG Network and it will stay this way.

The [Serving Catalog](https://github.com/kubernetes-sigs/wg-serving/tree/main/serving-catalog) work can be moved to the [Inference Perf](https://github.com/kubernetes-sigs/inference-perf) project. Originally it was designed for a larger scope, but was used mostly for Inference perf since.

The Inference Perf project is sponsored by SIG Scalability and no change of ownership is needed.

Cheers,  
Yuan Tang On behalf of Kubernetes WG Serving Co-Chairs
