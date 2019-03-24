---
layout:     post
title:      "TensorFlow - Not Just for Deep Learning"
subtitle:   "A Glance at Its Machine Learning Building Blocks and Collection of Algorithms"
date:       2016-08-06
author:     "Yuan Tang"
header-img: "img/inblog/tensorflow-bg.jpg"
tags:
    - Deep Learning
    - TensorFlow
    - Open Source
    - Machine Learning
    - Python
---

(Chinese translation [here (中文)](http://mp.weixin.qq.com/s?__biz=MzI0MDIxMDM0MQ==&mid=2247483724&idx=1&sn=3a8456395595ce20a8c826b40611961b&scene=0#wechat_redirect) by Xiatian)

One time when I was illustrating the [code base](https://github.com/tensorflow/tensorflow) and [architecture](http://arxiv.org/pdf/1603.04467.pdf) of [TensorFlow](https://www.tensorflow.org/) to my friends, they were quite surprised by how much more code was introduced since TensorFlow's first open-source release. They were only expecting several popular types of deep learning algorithms from the code base as heard from other people and social media. 

**Yet, TensorFlow is not just for deep learning**. It provides a great variety of building blocks for general numerical computation and machine learning. In this blog post, I will introduce the wide range of general machine learning algorithms and their building blocks provided by TensorFlow in `tf.contrib`. Note that many of the modules in `tf.contrib` will be moved to the main TensorFlow module once their interfaces are more stable. 

## High-level TF.Learn Estimators

[TF.Learn](https://www.tensorflow.org/versions/master/tutorials/tflearn/index.html) is a high-level module inside TensorFlow that provides various number of machine learning algorithms inside it's estimators module. Besides easy-to-use deep learning APIs such as Deep Neural Networks, Recurrent Neural Networks, etc, there are also a collection of popular machine learning algorithms. Currently, the following algorithms are included:

* [K-means clustering](https://github.com/tensorflow/tensorflow/blob/32bd3d024f33e920a67a1081bc0ae0048350fdee/tensorflow/contrib/factorization/python/ops/kmeans.py)
* [Random Forests](https://github.com/tensorflow/tensorflow/blob/v0.10.0rc0/tensorflow/contrib/learn/python/learn/estimators/random_forest.py)
* [Support Vector Machines](https://github.com/tensorflow/tensorflow/blob/v0.10.0rc0/tensorflow/contrib/learn/python/learn/estimators/svm.py)
* [Gaussian Mixture Model clustering](https://github.com/tensorflow/tensorflow/blob/32bd3d024f33e920a67a1081bc0ae0048350fdee/tensorflow/contrib/factorization/python/ops/gmm.py)
* [Linear](https://github.com/tensorflow/tensorflow/blob/v0.10.0rc0/tensorflow/contrib/learn/python/learn/estimators/linear.py)/[logistic regression](https://github.com/tensorflow/tensorflow/blob/v0.10.0rc0/tensorflow/contrib/learn/python/learn/estimators/logistic_regressor.py) 

More to come soon so stay tuned! To learn how to build your own machine learning estimator, please see my [previous post](http://terrytangyuan.github.io/2016/07/08/understand-and-build-tensorflow-estimator/). There are more official tutorials on TF.Learn [here](https://www.tensorflow.org/versions/master/tutorials/tflearn/index.html). 

## Statistical Distributions

A wide variety of statistical distributions functions are also provided by TensorFlow located inside `tf.contrib.distributions`, including but not limited to distributions like Bernoulli, Beta, Chi2, Dirichlet, Gamma, Uniform, etc. They are important building blocks when it comes to build machine learning algorithms, especially for probabilistic approaches like Bayesian models. 

## Layer Components

Inside `tf.contrib.layers`, there are functions that produce layer operations and associated weight and bias variables. These are mostly used for building different deep learning architectures. To name a few, there are functions for batch normalization, convolution layer, dropout layer, etc. There's also one-hot encoding used very often for machine learning tasks. 

Different optimizers such as Adagrad, SGD, Momentum, etc, are also included in this module located in `tf.contrib.layers.optimizers`. They are often used to solve optimization problems for numeric analysis, including optimizing parameter space to find a better model. 

Regularizers, such as L1 and L2 regularizations, available in `tf.contrib.layers.regularizers` module, are often used to reduce the risk of overfitting by penalizing the large number of features used in the model. It's used as building block for machine learning models such as Lasso and Ridge regression. 

Many algorithms, especially deep learning algorithms, require the calculation of gradients in order to optimize the model. It is common to initialize the model parameters randomly before starting to find the optimal parameters in the parameter space. TensorFlow provides several initializers such as Xavier initializer in `tf.contrib.layers.initializers`, used for weights to keep the scale of the gradients roughly the same in all layers. 

`tf.contrib.layers.feature_column` provides functionalities to transform both continuous and categorical features using methods like bucketing/binning, crossing/compostion, and embedding. You can have a glance at an example application explained in [Wide and Deep Learning Tutorial](https://www.tensorflow.org/versions/r0.10/tutorials/wide_and_deep/index.html). There are additional functions in `tf.contrib.layers.embedding` that convert high-dimensional categorical features into a low-dimensional and dense real-valued vector, often referred to as an embedding vector. These low-dimensional dense embedding vectors are concatenated with the continuous features that get fed into the model. 

## Loss Functions and Metrics

Machine learning algorithms rely on optimizations based the loss function provided. TensorFlow provides a wide range of loss functions to choose inside `tf.contrib.losses`, such as sigmoid and softmax cross entropy, log-loss, hinge loss, sum of squares, sum of pairwise squares, etc. 

A variety types of metrics are available in `tf.contrib.metrics`, such as precision, recall, accuracy, auc, MSE, as well as their streaming versions. 

## Others

Note that I only highlighted a few important components to help you get a sense of what's inside TensorFlow's contrib module. There more functionalities such as `DataFrame` and `Monitors` to facilitate some machine learning process as described in my previous blog on [high-level learn modules](http://terrytangyuan.github.io/2016/06/09/scikit-flow-v09/). 

## More Resources:

* [Building Machine Learning Estimator in TensorFlow](http://terrytangyuan.github.io/2016/07/08/understand-and-build-tensorflow-estimator/)
* [TensorFlow Official Tutorials on TF.Learn](https://www.tensorflow.org/versions/master/tutorials/tflearn/index.html)
* [Key Features of Scikit Flow Illustrated](http://terrytangyuan.github.io/2016/03/14/scikit-flow-intro/)
* [High-level Learn Module in TensorFlow](http://terrytangyuan.github.io/2016/06/09/scikit-flow-v09/)
* [Scikit Flow: Easy Deep Learning with TensorFlow and Scikit-learn](http://www.kdnuggets.com/2016/02/scikit-flow-easy-deep-learning-tensorflow-scikit-learn.html)


<p class="copyright text-muted">
	Copyright &copy; {{ site.title }} {{ site.time | date: '%Y' }}
</p>
<br><b>Banner Credit to TensorFlow Org</b>
