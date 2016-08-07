---
layout:     post
title:      "TensorFlow - Not Just for Deep Learning"
subtitle:   "A Glance at Its Machine Learning Building Blocks and Algorithms"
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

One time when I was illustrating the code base of TensorFlow to my friends, they were quite surprised by how much more code was introduced since TensorFlow's first open-source release. They were only expecting all kinds of deep learning algorithms from the codebase as heard from other people and social media. 

Yet, TensorFlow is not just for deep learning. In this blogpost, I will introduce the wide range of general machine learning algorithms and their building blocks provided by TensorFlow. 

## High-level TF.Learn Estimators

TF.Learn is a high-level module inside TensorFlow that provides various number of machine learning algorithms inside it's estimators module. Besides easy-to-use deep learning APIs such as Deep Neural Networks, Recurrent Neural Networks, etc, there are also a collection of popular machine learning algorithms. To name a few, there are K-means clustering, Random Forests, Support Vector Machines, Gaussian Mixture Model clustering, linear/logistic regression, and more to come soon. 

Learn how to build your own machine learning estimator, see my previous post. 
## Statistical Distributions

Machine learning 


* Statistical Distributions in tf.contrib.distributions
    - Bernoulli, Beta, Chi2, Dirichlet, Gamma, Uniform, etc
* tf.contrib.layers
    - Deep Learning layers, e.g. batch_norm, convolution, dropout, etc
    - one-hot encoding
    - optimizers, e.g. Adagrad, SGD, Momentum, etc (some are used for ML)
    - regularizers, e.g. L1, L2
    - initializers, variance_scaling_initializer, xavier_initializer
    - feature column, categorical features, continuous features, etc
    - embeddings
    - target column, extract target column for different ML problems
* tf.learn dataframe
* tf.contrib.losses
    - sigmoid_cross_entropy, softmax_cross_entropy, log loss, hinge loss, sum of squares, sum_of_pairwise_squares, etc
* tf.contrib.metrics
    - precision, recall, accuracy, auc, MSE, etc

<br><b>Copyright Reserved Yuan Tang 2016</b>
<br><b>Banner Credit to TensorFlow Org</b>
