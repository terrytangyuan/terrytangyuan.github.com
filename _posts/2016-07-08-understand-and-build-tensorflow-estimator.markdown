---
layout:     post
title:      "Building Customized Machine Learning Estimator in TensorFlow"
subtitle:   "with Scikit-learn Style"
date:       2016-07-08
author:     "Yuan Tang"
header-img: "img/inblog/tensorflow-bg.jpg"
tags:
    - Deep Learning
    - TensorFlow
    - Open Source
    - Machine Learning
    - Python
--- 


## Distributed TensorFlow Estimator

With the great addition of [graph_actions module](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/learn/python/learn/graph_actions.py) that handles most of the complicated distributed logics of model training and evaluation, the [estimators](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/learn/python/learn/estimators) now incorporates `Supervisor` and `Coordinator` logics to train models in a distributed fasion. `Estimator` now accepts custom model function that accepts various signatures, such as the following:

* `(features, targets) -> (predictions, loss, train_op)`
* `(features, targets, mode) -> (predictions, loss, train_op)`
* `(features, targets, mode, params) -> (predictions, loss, train_op)`

Basically `train_op` can be specified instead of using `learn.trainer` internally so users are able to specify more customized things and a lot of high-levels in `contrib` folder can be utilized as well. You can inherit from basic estimator and build your own estimators that suit your needs without worrying about implementation details on communications between different threads and setting up a master supervisor. Please see the documentation for `Estimator` for most updated docs. You can find the work-in-progress API guides [here](https://www.tensorflow.org/versions/master/api_docs/python/contrib.learn.html). 

## Understanding `BaseEstimator` and `Estimator`

`BaseEstimator` is the abstract and base class for training and evaluating TensorFlow models. It provides the basic functionalities like `fit()`, `partial_fit()`, `evaluate()`, and `predict()` by utilizing detailed logics hidden in `graph_actions.py` to handle model inference, evaluation, and training, as well as `data_feeder.py` to handle data batches fetching for different types of input (Note: in the future, `DataFeeder` will be replaced by `learn.DataFrame`). It also checks for compatibility of inputs in terms of `dtypes` and whether inputs are sparse using `estimators.tensor_signature`. In the meantime, `BaseEstimator` intializes the settings for monitors, checkpointing, etc. While providing most of the logics required for building and evaluating a customized model function, it leaves implementations for `_get_train_ops()`, `_get_eval_ops()`, and `_get_predict_ops()` to its sub-classes, in order to give freedom to sub-classes that require custom handling. 

`Estimator` implemented in the module is the perfect example of how to implement those functions that are left to be overriden by sub-classes of `BaseEstimator`. 

For example, `_get_train_ops()` in `Estimator` takes features and targets as inputs, and then returns a tuple of train `Operation` and loss `Tensor`, using the customized model function. 






```python

```



## More Resources:

* [Introduction to Scikit Flow and why you want to start learning TensorFlow](https://medium.com/@ilblackdragon/tensorflow-tutorial-part-1-c559c63c0cb1)
* [DNNs, custom model and Digit recognition examples](https://medium.com/@ilblackdragon/tensorflow-tutorial-part-2-9ffe47049c92)
* [Categorical variables: One hot vs Distributed representation](https://medium.com/@ilblackdragon/tensorflow-tutorial-part-3-c5fc0662bc08)
* [Scikit Flow: Easy Deep Learning with TensorFlow and Scikit-learn](http://www.kdnuggets.com/2016/02/scikit-flow-easy-deep-learning-tensorflow-scikit-learn.html)
* [Key Features of Scikit Flow Illustrated](http://terrytangyuan.github.io/2016/03/14/scikit-flow-intro/)

Note: a work-in-progress documentation page can be found [here](https://www.tensorflow.org/versions/master/api_docs/python/contrib.learn.html). 

We welcome any contributions to this exciting project. No matter if it's simple typos, bug fixes/reports, or suggestions on enhancements and future directions. Do not hesitate to ask me if you'd like to see certain things in my future blogs. 

<br><b>Copyright Reserved Yuan Tang 2016</b>
