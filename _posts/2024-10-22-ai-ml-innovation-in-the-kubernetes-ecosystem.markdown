---
layout:     post
title:      "AI/ML Innovation in the Kubernetes Ecosystem"
subtitle:   "Recent innovations like the Model Registry, ModelCars feature, and TrustyAI are delivering manageability, speed, and accountability for AI/ML workloads"
date:       2024-10-22
author:     "Yuan Tang"
tags:
    - Open Source
    - Kubernetes
    - Artificial Intelligence
---

*This blogpost was originally posted [here](https://dzone.com/articles/ai-ml-innovation-in-the-kubernetes-ecosystem).*

As organizations put artificial intelligence and machine learning (AI/ML) workloads into continuous development and production deployment, they need to have the same levels of manageability, speed, and accountability as regular software code. The popular way to deploy these workloads is Kubernetes, and the [Kubeflow](https://www.kubeflow.org/) and [KServe](https://kserve.github.io/website/latest/) projects enable them there. Recent innovations like the Model Registry, ModelCars feature, and TrustyAI integrations in this ecosystem are delivering these improvements for users who rely on AI/ML. These, and other improvements, have made open source AI/ML ready for use in production. More improvements are coming in the future.

## Better Model Management

AI/ML analyzes data and produces output using machine learning "models," which consist of code, data, and tuning information. In 2023, the Kubeflow community [identified a key requirement](https://blog.kubeflow.org/kubeflow-user-survey-2023/) to have better ways of distributing tuned models across large Kubernetes clusters. Engineers working on Red Hat's OpenShift AI agreed and started work on a new Kubeflow component, [Model Registry](https://github.com/kubeflow/model-registry).

"The Model Registry provides a central catalog for developers to index and manage models, their versions, and related artifacts metadata," explained Matteo Mortari, Principal Software Engineer at Red Hat and Kubeflow contributor. "It fills a gap between model experimentation and production activities, providing a central interface for all users to effectively collaborate on ML models."

The AI/ML model development journey, from initial experimentation to deployment in production, requires coordination between data scientists, operations staff, and users. Before Model Registry, this involved coordinating information scattered across many places in the organization – even email! With Model Registry, system owners can implement efficient machine learning operations (MLOps), letting them deploy directly from a dedicated component. It's an essential tool for researchers looking to run many instances of a model across large Kubernetes clusters. The project is currently in Alpha, and was included in the recent [Kubeflow 1.9 release](https://blog.kubeflow.org/kubeflow-1.9-release/).

## Faster Model Serving

Kubeflow makes use of the KServe project to "serve," or run, models on each server in the Kubernetes cluster. Users care a great deal about latency and overhead when serving models: they want answers as quickly as possible, and there's never enough GPU power. Many organizations have service level objectives (SLO) for response times, particularly in regulated industries.

"One of the challenges that we faced when we first tried out LLMs on Kubernetes was to avoid unnecessary data movements as much as possible," said Roland Huss, Senior Principal Software Engineer at Red Hat and KServe and Knative contributor. "Copying over a multi-gigabyte model from an external storage can take several minutes which adds to the already lengthy startup of an inference service. Kubernetes itself knows how to deal with large amounts of data when it comes to container images, so why not piggyback on those matured techniques?"

This thinking led to the development of [Modelcars](https://kserve.github.io/website/latest/modelserving/storage/oci/#using-modelcars), a passive "sidecar" container holding the model data for KServe. That way, a model needs to be present only once at a cluster node, regardless how many replicas are accessing it. Container image handling is a very well explored area in Kubernetes, with sophisticated caching and performance optimization for the image handling. The result has been faster startup times for serving models, and greatly reduced disk space requirements for cluster nodes.

Huss also pointed out that Kubernetes 1.31 recently introduced an image volume type that allows the direct mount of OCI images. When that feature is generally available, which may take a year, it can replace ModelCar for even better performance. Right now, ModelCar is available in KServe v0.12 and above.

## Safer Model Usage

AI/ML systems are complex, and it can be difficult to figure out how they arrive at their output. Yet it's important to ensure that unexpected bias or logic errors don't create misleading results. [TrustyAI](https://trustyai-explainability.github.io/) is a new open source project which aims to bring "responsible AI" to all stages of the AI/ML development lifecycle.

"The TrustyAI community strongly believes that democratizing the design and research of responsible AI tooling via an open source model is incredibly important in ensuring that those affected by AI decisions – nowadays, basically everyone – have a say in what it means to be responsible with your AI," stated Rui Vieira, Senior Software Engineer at Red Hat and TrustyAI contributor.

The project uses an approach where a core of techniques/algorithms, mostly focused on AI explainability, metrics and guardrails, can be integrated at different stages of the lifecycle. For example, a Python TrustyAI library can be used through Jupyter notebooks during the model experimentation stage to identify biases. The same functionality can be also used for continuous bias detection of production models by incorporating the tool as a pipeline step before model building or deployment.

TrustyAI is in its second year of development and [KServe supports TrustyAI](https://kserve.github.io/website/master/modelserving/explainer/trustyai/).

## Future AI/ML Innovations

With these features and tools, and others, development and deployment of AI/ML models is becoming more consistent, reliable, efficient, and verifiable. As with other generations of software, this allows organizations to adopt and customize their own open source AI/ML stacks that would have been too difficult or risky before.

The Kubeflow and KServe community is working hard on the next generation of improvements, usually in the [Kubernetes Serving Working Group (WG Serving)](https://github.com/kubernetes/community/tree/master/wg-serving). This includes the [LLM Serving Catalog](https://github.com/kubernetes-sigs/wg-serving/tree/main/serving-catalog), to provide working examples for popular model servers and explore recommended configurations and patterns for inference workloads. WG Serving is also exploring the [LLM Instance Gateway](https://github.com/kubernetes-sigs/llm-instance-gateway) to more efficiently serve distinct LLM use cases on shared model servers running the same foundation model, allowing scheduling requests to pools of model servers.  

The KServe project is working on features to support very large models. One is multi-host/multi-node support for models which are too big to run on a single node/host. Support for "Speculative Decoding," another in-development feature, speeds up large model execution and improves inter-token latency in memory-bound LLM inference. The project is also developing "LoRA adapter" support which permits serving already trained models with in-flight modifications via adapters to support distinct use cases instead of re-training each of them from scratch before serving. The KServe community is also working on Open Inference Protocol extension to GenAI Task APIs that provide community-maintained protocols to support various GenAI task specific APIs. The community is also working closely with WG Serving to integrate with the efforts like LLM Instance Gateway and provide KServe examples in the Serving Catalog. These and other features are in the [KServe Roadmap](https://github.com/kserve/kserve/blob/master/ROADMAP.md).

The author will be delivering a keynote about some of these innovations at [KubeCon's Cloud Native AI Day](https://colocatedeventsna2024.sched.com/event/1jOWl) in Salt Lake City. Thanks to all of the ingenuity and effort being poured into open source AI/ML, users will find the experience of building, running, and training models to keep getting more manageable and performant for many years to come.
