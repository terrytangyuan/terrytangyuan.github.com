---
layout:     post
title:      "DeepMind TF-Replicator Simplifies Model Deployment on Cluster Architectures"
subtitle:   "Thoughts on DeepMind TF-Replicator with Synced"
date:       2019-03-20
author:     "Yuan Tang"
tags:
    - Deep Learning
    - Machine Learning
    - Kubeflow
    - TensorFlow
    - Kubernetes
    - Interview
    - Open Source
---

*This article is cross-posted from [Synced on Medium](https://medium.com/syncedreview). The original post can be found [here](https://medium.com/syncedreview/deepmind-tf-replicator-simplifies-model-deployment-on-cluster-architectures-c6ab5fcb85ee).*

DeepMind’s Research Platform Team has open-sourced TF-Replicator, a framework that enables researchers without previous experience with the distributed system to deploy their TensorFlow models on GPUs and [Cloud TPUs](https://cloud.google.com/tpu/). The move aims to strengthen AI research and development.

> “TF-Replicator simplifies writing data-parallel and model-parallel research code. The same models can be effortlessly deployed to different cluster architectures (i.e. one or many machines containing CPUs, GPUs or TPU accelerators) using synchronous or asynchronous training regimes. To demonstrate the generality and scalability of TF-Replicator, we implement and benchmark three very different models: (1) A ResNet-50 for ImageNet classification, (2) a SN-GAN for class-conditional ImageNet image generation, and (3) a D4PG reinforcement learning agent for continuous control. Our results show strong scalability performance without demanding any distributed systems expertise of the user.” (arXiv).

**Synced invited Yuan Tang, a senior software engineer at Ant Financial, to share his thoughts on TF-Replicator.**

**How would you describe TF-Replicator?**

TF-Replicator is a framework to simplify the writing of distributed TensorFlow code for training machine learning models, so that they can be effortlessly deployed to different cluster architectures.

**Why does this TF-Replicator matter?**

Though TensorFlow provides direct support for CPU, GPU, and TPU devices, it is often non-trivial to switch between different devices as this requires writing specialized code for a particular hardware and puts research constraints on that particular platform. For example, incorrect handling of state often leads to silent errors, and coordinating heterogeneous behavior among replicas requires additional complexity during implementation.

There have been significant efforts in TensorFlow such as [TensorFlow Estimators](https://arxiv.org/abs/1708.02637) to make this easier for production use cases, but these often lack the necessary flexibility and expressivity for experimenting with new distributed strategies on different platforms during research. TF-Replicator provides an easy-to-use API that hides the complexity of low-level, device-specific API such as the existing TensorFlow TPU API, which greatly lowers the barrier to TPU adoption. Since TensorFlow 2.0, TF-Replicator has been integrated into [tf.distribute.Strategy API](https://www.tensorflow.org/alpha/guide/distribute_strategy) and can be used effortlessly in combination with [tf.estimator](https://www.tensorflow.org/guide/estimators) and [tf.keras](https://www.tensorflow.org/guide/keras).

**What impact might this research bring to the research community?**

Most recent AI breakthroughs, such as [AlphaStar](https://deepmind.com/blog/alphastar-mastering-real-time-strategy-game-starcraft-ii/) that masters the real-time strategy game [StarCraft II](https://starcraft2.com/en-us/) , often require reliable and scalable machine learning infrastructures. The huge amounts of data involved in training, the need to train ever-larger neural networks with new capabilities, and the complications of running high intensity computations on heterogeneous and distributed systems have prevented the most advanced methods from being widely adopted in production. TF-Replicator greatly lowers the barrier to experiment and adopt different hardware accelerators. It allows researchers to iterate on new research ideas and deploy the trained models to different cluster architectures efficiently.

Additionally, TF-Replicator provides convenient methods such as a wrapper for [tf.train.Optimizer](https://www.tensorflow.org/api_docs/python/tf/train/Optimizer), so that gradients are accumulated across devices before updating model parameters. TF-Replicator also provides communication patterns such as [MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface)-like primitives similar to DistributedOptimizer in [Horovod](https://github.com/uber/horovod). All of these make it much easier to perform cross-replica communication of gradients and to implement operations such as global batch normalization that’s used to scale up training of DeepMind’s [BigGAN](https://arxiv.org/abs/1809.11096) models. The components implemented within TF-Replicator can also be reused to experiment with new distributing strategies.

**Can you identify any bottlenecks in the research?**

Researchers can use [tf.estimator](https://www.tensorflow.org/guide/estimators) and [tf.keras](https://www.tensorflow.org/guide/keras) to quickly iterate on new model implementations while using TF-Replicator through [tf.distribute.Strategy API](https://www.tensorflow.org/alpha/guide/distribute_strategy) to leverage different distributed strategies. TF-Replicator and other shared infrastructure allow researchers to build increasingly complex experiments on robust foundations and quickly spread best practices among the collaborators. However, TF-Replicator is tightly coupled with TensorFlow and companies that heavily rely on other frameworks such as [PyTorch](https://pytorch.org/) and [Apache MXNet](https://mxnet.apache.org/) would not be able to leverage the same framework. For example, PyTorch has its own distributed communication package, [torch.distributed](https://pytorch.org/docs/stable/distributed.html), that supports different backends such as [Gloo](https://github.com/facebookincubator/gloo), [MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface), and [NCCL](https://developer.nvidia.com/nccl).

As of the time of writing, the tf.distribute.Strategy API in TensorFlow 2.0 alpha release supports training with tf.estimator using all available distributed strategies. However, it only supports training with tf.keras using MirroredStrategy and ParameterServerStrategy. If users need to use other strategies like TPUStrategy and MultiWorkerMirorredStrategy, they would have to disable [eager execution](https://www.tensorflow.org/guide/eager). In addition, tf.keras users would have to explicitly shard or shuffle the data for different workers, which isn’t very user-friendly.

**Can you predict any potential future developments related to this research?**

Though tf.distribute.Strategy API in TensorFlow 2.0 alpha release has certain limitations when used together with tf.keras, the TensorFlow team has been actively working on improvements. Rest assured that once the additional strategies are supported, the API will look the same. The modules responsible for distributed training strategies in different frameworks (e.g. TensorFlow, PyTorch and Apache MXNet) would likely become more and more similar to each other. We should expect to see a more diverse set of distributed strategies as more feedback is collected from the community of users and advancements are made in this research area.

**What are the next steps after using TF-Replicator to define the distributed TensorFlow training program?**

After the distributed TensorFlow training program has been defined using TF-Replicator or tf.distribute.Strategy API, no further action is required for multi-GPU synchronous local training. For multi-GPU synchronous local training, variables are not mirrored and instead are placed on the CPU and operations are replicated across all local GPUs. However, if users want to train in multiple workers, they have to create a cluster with multiple workers on an external IP address and specify TF_CONFIG environment variable to configure each worker appropriately. Users could leverage tools such as [Kubeflow](https://www.kubeflow.org/) based on [Kubernetes](https://kubernetes.io/) to facilitate the process. Kubeflow provides operators such as [tf-operator](https://github.com/kubeflow/tf-operator) and [mpi-operator](https://github.com/kubeflow/mpi-operator) that could take TensorFlow code with tf.distribute.Strategy or Horovod’s DistributedOptimizer to scale to multiple workers effortlessly. There’s also the Kubernetes template in [tensorflow/ecosystem](https://github.com/tensorflow/ecosystem) repo which sets TF_CONFIG for the training tasks.

The paper *TF-Replicator: Distributed Machine Learning for Researchers* is on [arXiv](https://arxiv.org/abs/1902.00465).

## Synced Insight Partner Program

The Synced Insight Partner Program is an invitation-only program that brings together influential organizations, companies, academic experts and industry leaders to share professional experiences and insights through interviews and public speaking engagements, etc. Synced invites all industry experts, professionals, analysts, and others working in AI technologies and machine learning to participate.


<p class="copyright text-muted">
	Copyright &copy; {{ site.title }} {{ site.time | date: '%Y' }}
</p>
