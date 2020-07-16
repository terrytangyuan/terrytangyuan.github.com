---
layout:     post
title:      "如何参与TensorFlow社区开源贡献"
subtitle:   ""
date:       2020-07-15
author:     "Yuan Tang"
tags:
    - Open Source
    - Kubernetes
    - Kubeflow
    - Machine Learning
    - Deep Learning
---

[知乎原文链接](https://www.zhihu.com/question/399226479/answer/1329044228)


作为最早一批非谷歌的TensorFlow社区贡献者，也是 TensorFlow committer + SIG IO maintainer。我在这里分享一下自己贡献 TensorFlow 的经历，希望能对大家有启发，鼓励大家一起参与进来。大家如果感兴趣可以去[我的GitHub页面](https//github.com/terrytangyuan)查找相关的贡献，以及关注[我的Twitter](https//twitter.com/terrytangyuan)来得到第一时间的更新。

我最早参与的项目是 [tensorflow/skflow](https://github.com/tensorflow/skflow) (Scikit Flow)，这是当时谷歌工程师 Illia Polosukhin 最早创立的项目，我在很早期就开始参与，主要贡献了许多新的API的设计以及用户体验的提升。这个模块的目的是降低大家使用分布式机器学习和深度学习的门槛，让大家可以像使用 Scikit-learn 那样快速地搭建自己的机器学习和深度学习模型，用仅仅几行代码就能使用 TensorFlow 实现的深度学习算法，甚至是传统的机器学习算法，比如逻辑回归、随机森林、等等。而且可以很方便地部署到分布式的集群中，从而真正地使用到 TensorFlow 的分布式训练优势。当时在早期的 TensorFlow 版本中都是需要对低阶的 API 有深度的理解才能实现这些。数据科学从事者没有必要为了使用最新的算法和技术花许多时间来学习这些实现的细节，通过这一套高阶的 API，他们可以很快地直接将这些使用在工作和研究中。当时作为数据科学从事者的一员，看到了这一块的需求，即使自己比较熟悉 TensorFlow 也仍然感到实现算法特别繁琐。TensorFlow 团队也意识到了高阶 API 对社区用户的重要性，我们把 Scikit Flow 贡献到了 [tf.estimator 模块](https://www.tensorflow.org/guide/estimator)，后来也开始积极地参与进来，改进了很多分布式训练的逻辑，更好地和 TensorFlow 生态融合，关于模块的设计，可以参考我们的 KDD 2017 文章 [《TensorFlow Estimators: Managing Simplicity vs. Flexibility in High-Level Machine Learning Frameworks》](https://arxiv.org/abs/1708.02637)。当时由于我对 TensorFlow 的贡献，谷歌颁给了我 Open Source Peer Bonus，这个是由内部员工提名推荐，然后再经过内部审核和讨论得到最后的获奖人名单的，我通过持续对 TensorFlow 的贡献吸引到了他们的注意最后得到肯定，这是对我的一个很大的鼓励以及对我的贡献的认可，在这里鼓励大家重在坚持，相信一切的付出都是值得的。

TensorFlow 社区现在也分为了很多子项目以及不同的特别兴趣小组 SIGs，比如 SIG Networking、SIG IO、等等，大家可以参考社区 [tensorflow/community](https://github.com/tensorflow/community) 里的一些文档积极参与进来，新的设计方案也会通过 RFC 的形式公开和社区讨论。[TensorFlow I/O](https://github.com/tensorflow/io) 支持 TensorFlow 从各种格式以及文件系统来读写数据，作为 maintainer 一员，在这里也邀请大家在使用的同时，有什么问题和想法都可以在社区提出来，贡献不仅仅限于贡献代码，很多时候贡献文档、参与讨论也会给社区带来非常大的帮助。

参与 TensorFlow 社区贡献，也不仅仅限于 TensorFlow GitHub 组织下的项目，在这我也简单介绍一下在加入 TensorFlow 社区之后围绕 TensorFlow 生态做的许多的工作。

*  [Kubeflow](https://github.com/kubeflow/) 支持在 Kubernetes 集群上很方便地运行各种机器学习框架，这其中也包括通过 [TF Operator](https://github.com/kubeflow/tf-operator) 执行 TensorFlow 原生分布式训练、通过 [MPI Operator](https://github.com/kubeflow/mpi-operator) 执行 Horovod 支持的 TensorFlow 分布式训练 (参考 [KubeFlow MPI-Operator深度解读](https://zhuanlan.zhihu.com/p/133628984) by @薛磊)、通过 Katib 来提供云原生的自动机器学习 (参考 [Katib 论文解读](https://zhuanlan.zhihu.com/p/157589799) by @高策)
* [ElasticDL](https://github.com/sql-machine-learning/elasticdl) 支持在 Kubernetes 集群上运行 TensorFlow，并且支持容错和弹性调度，提升集群利用率 (参考 [ElasticDL: 同时提升集群利用率和研发效率的分布式深度学习框架](https://zhuanlan.zhihu.com/p/157998796) by ElasticDL 团队 @王益 @齐俊 @章海涛 @looong @gml)。
* 和 RStudio 合作的 [TensorFlow in R](https://tensorflow.rstudio.com/)，提供了非常友好的 API 让 R 语言用户能方便地使用 TensorFlow，包括所有的低阶 API，也包括 tf.keras、tf.data、tf.estimator 等等。

当时参与贡献比较早，TensorFlow 文档和教材也都是以英文为主，我也写了当时第一本 TensorFlow 中文教材[《TensorFlow实战》](https://terrytangyuan.github.io/2017/02/12/tensorflow-in-practice-book-chinese/)，具体的动机和背景可以参考 [CSDN 的专访](https://terrytangyuan.github.io/2019/12/31/interview-with-csdn-year-end/)。最近也参与了《动手学深度学习》英文版的 TensorFlow 实现，具体参考 @李沐 的官宣 [《动手学深度学习》新增TensorFlow实现](https://zhuanlan.zhihu.com/p/157675926)，项目开源在 [d2l-ai/d2l-en](https://github.com/d2l-ai/d2l-en)，在这里也鼓励大家一起参与进来，让好的知识和技术能够得到更好更快地传播。


<p class="copyright text-muted">
	Copyright &copy; {{ site.title }} {{ site.time | date: '%Y' }}
</p>

