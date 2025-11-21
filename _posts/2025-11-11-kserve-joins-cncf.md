---
layout:     post
title:      "KServe Joins CNCF as an Incubating Project"
subtitle:   ""
date:       2025-11-11
author:     "Yuan Tang"
tags:
    - Open Source
    - Kubernetes
    - Artificial Intelligence
    - Machine Learning
    - KServe
---

*Originally posted on [Red Hat Blog](https://www.redhat.com/en/blog/kserve-joins-cncf-incubating-project). In addition, check out the complementary [announcement blog from CNCF](https://www.cncf.io/blog/2025/11/11/kserve-becomes-a-cncf-incubating-project/)*.


We are excited to share that [KServe](https://kserve.github.io/website/), the leading standardized AI inference platform on Kubernetes, [has been accepted as an incubating project](https://www.cncf.io/blog/2025/11/11/kserve-becomes-a-cncf-incubating-project/) by the Cloud Native Computing Foundation (CNCF).

This milestone validates KServe’s maturity, stability and role as the foundation for scalable, multi-framework model serving in production environments. By moving into the CNCF’s neutral governance, KServe’s development will be driven purely by community needs, accelerating its standardization for serving AI models on Kubernetes.

For Red Hat this is a validation of our commitment to delivering open, reliable and standardized AI solutions for the hybrid cloud.

**The critical engine behind Red Hat OpenShift AI**

At Red Hat, we believe the best AI infrastructure is built on open standards and Kubernetes. KServe is the critical model serving component that powers Red Hat OpenShift AI, helping ensure our customers can transition from model experimentation to production inference seamlessly and at scale.

OpenShift AI leverages KServe’s features to solve the biggest enterprise AI challenges, helping enterprises realize:

* **High-performance LLM optimization \-** KServe is optimized for large language models (LLMs), providing high-performance features like KV cache offloading, distributed inference with vLLM, as well as disaggregated serving, pre-fix caching, intelligent scheduling and variant autoscaling via the integration with llm-d.   
* **Advanced autoscaling \-** In addition to the horizontal pod autoscaling capability from Kubernetes, KServe also supports autoscaling with KEDA (Kubernetes Event-driven Autoscaler), which enables event-driven scaling based on external metrics such as vLLM metrics.  
* **Both predictive and generative AI model inference \-** KServe supports pluggable, reusable, extensible runtimes, ranging from scikit-learn and XGBoost for predictive AI to Hugging Face and vLLM for generative AI model inference. This helps ensure that enterprises can switch to the best runtime for specific use cases.

**Unlocking enterprise AI value**

The journey of AI from the lab to the bottom line requires production infrastructure that can handle exponential growth, especially as enterprise usage shifts to widespread generative applications.

Now bolstered by the full resources and neutral governance of the CNCF, KServe directly addresses these core operational challenges \- from tackling complexity with a unified API to controlling cloud costs through its scale-to-zero capabilities.

This move offers enterprises confidence in the longevity, security and open future of their AI infrastructure investment. KServe is now positioned to be the open-source standard for cloud-native model serving, empowering enterprises to confidently build, deploy and scale the next generation of intelligent applications on a foundation of open standards and community-driven innovation.

## **Join the Movement\!**

We invite the community to join us in congratulating the KServe maintainers and contributors on this achievement.

Want to get involved and shape the future of AI inference? Here’s how you can join the journey:

Check out KServe GitHub repo: [https://github.com/kserve/kserve](https://github.com/kserve/kserve)  
Join KServe community: [https://github.com/kserve/community](https://github.com/kserve/community) 

Additionally, join us at our KubeCon+CloudNativeCon NA sessions to hear more about KServe:

[Anchoring Trust in the Age of AI: Identities Across Humans, Machines, and Models](https://sched.co/27dCb) \- Tuesday November 11, 2025 10:08 am ET

