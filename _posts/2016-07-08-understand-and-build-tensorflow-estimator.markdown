---
layout:     post
title:      "Building Machine Learning Estimator in TensorFlow"
subtitle:   "Understanding the Internals of TensorFlow Learn Estimators"
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

(This blog is featured in DataScienceWeekly [here](http://www.datascienceweekly.org/newsletters/data-science-weekly-newsletter-issue-138) and Chinese translation [here (中文)](http://mp.weixin.qq.com/s?__biz=MzI0MDIxMDM0MQ==&mid=2247483708&idx=1&sn=825a95910aeb14a9b0b769a9321d4177#wechat_redirect) by Xiatian)

Have you ever wondered what's the magic behind the tutorials on [Large-scale Linear Models](https://www.tensorflow.org/versions/master/tutorials/linear/overview.html#large-scale-linear-models-with-tensorflow) and [Wide & Deep Learning](https://www.tensorflow.org/versions/master/tutorials/wide_and_deep/index.html#tensorflow-wide-deep-learning-tutorial)? I hope this post would at least point you to the right direction. 

Please take a look at my previous blog posts to understanding some basics of TensorFlow Learn and its integration with other high-level TensorFlow modules. 

The purpose of this post is to help you better understand the underlying principles of estimators in [TensorFlow Learn](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/learn/python/learn) and point out some tips and hints if you ever want to build your own estimator that's suitable for your particular application. This post will be helpful when you ever wonder how everything works internally and gets overwelmed by the large codebase. 

## Understanding `BaseEstimator` and `Estimator`

`BaseEstimator` is the abstract and base class for training and evaluating TensorFlow models. It provides the basic functionalities like `fit()`, `partial_fit()`, `evaluate()`, and `predict()` by utilizing detailed logics hidden in `graph_actions.py` to handle model inference, evaluation, and training, as well as `data_feeder.py` to handle data batches fetching for different types of input (Note: in the future, `DataFeeder` will be replaced by `learn.DataFrame`). It also checks for compatibility of inputs in terms of `dtypes` and whether inputs are sparse using `estimators.tensor_signature`. 

In the meantime, `BaseEstimator` intializes the settings for monitors, checkpointing, etc. While providing most of the logics required for building and evaluating a customized model function, it leaves implementations for `_get_train_ops()`, `_get_eval_ops()`, and `_get_predict_ops()` to its sub-classes, in order to give freedom to sub-classes that require custom handling. `BaseEstimator` is also distributed, I've discussed briefly in my previous blogpost [here](http://terrytangyuan.github.io/2016/06/09/scikit-flow-v09/).

`Estimator` implemented in the module is the perfect example of how to implement those functions that are left to be overriden by sub-classes of `BaseEstimator`. 

For example, `_get_train_ops()` in `Estimator` takes `features` and `targets` as inputs, and then returns a tuple of train `Operation` and loss `Tensor`, using the customized model function. If you want to implement your own estimator, this also gives you freedom to decide whether `targets` can be ignored if the estimator can be trained in unsupervised fashion. 

Similarly, `_get_eval_ops()` lets a sub-class to use customized metrics to evaluate each training step. A list of available metrics can be found in a couple of high-level modules in TensorFlow. It should return a dictionary of `Tensor` object that represents the evaluation ops for the metrics specified.

`_get_predict_ops()` is implemented to customize predictions, e.g. probability v.s. actual prediction output. It returns a `Tensor` or a dictionary of `Tensor` object that represents prediction ops. You can then easily use super-class's `predict()` to achieve functionalities like `transform()` similar to the one in Scikit-learn for unsupervised problems. 


## Examples of Estimators

### `LogisticRegressor`

`Estimator` already provides most of the implementations you need. For example, `LogisticRegressor` only needs to provide its own metrics, such as AUC, accuracy, precision and recall, dedicated for only binary classification problems. So later a user can sub-class `LogisticRegressor` to implement a estimator for binary classification without much further effort. 

### `TensorForestEstimator`

A `TensorForestEstimator` has also been added to TensorFlow Learn recently. It hides most of the detailed implementations of Random Forests in `contrib.tensor_forest` while utilizing some exposed high-level components to build the estimator so users can use `contrib.tensor_forest` more easily. 

For example, instead of passing all hyper-parameters to the contructor of `TensorForestEstimator`, they are passed into `params` in the contructor and the `params` are filled by `params.fill()` and later it will be used in Tensor Forest's own `RandomForestGraphs` for constructing the whole graph. 

```python
class TensorForestEstimator(estimator.BaseEstimator):
  """An estimator that can train and evaluate a random forest."""

  def __init__(self, params, device_assigner=None, model_dir=None,
               graph_builder_class=tensor_forest.RandomForestGraphs,
               master='', accuracy_metric=None,
               tf_random_seed=None, verbose=1,
               config=None):
    self.params = params.fill()
```

Since there are a lot of more details for implementation of Random Forest's inference (many of them have been written as separate kernels to speed things up), its `_get_predict_ops()` utilizes `tensor_forest.RandomForestGraphs` as its graph builder. It calls `graph_builder.inference_graph` to get the prediction ops. 


```python
def _get_predict_ops(self, features):
    graph_builder = self.graph_builder_class(
        self.params, device_assigner=self.device_assigner, training=False,
        **self.construction_args)
    features, spec = data_ops.ParseDataTensorOrDict(features)
    return graph_builder.inference_graph(features, data_spec=spec)
```

Similarly, it uses `graph_builder.training_loss` for the implementation of `_get_train_ops()`. Note that `TensorForestEstimator` uses functions in `tensor_forest.data.data_ops` module, such as `ParseDataTensorOrDict` and `ParseLabelTensorOrDict` to parse the input features and labels. 


## Other Examples

A new estimator for K-means clustering has been added today, located in `contrib.factorization.python.ops.kmeans`. Similar to `TensorForestEstimator`, dedicated kernels are written to highly optimize the speed and only some of the surfaced high-level components are used for the implementation of the estimator. More examples of implementing different estimators can be found in `learn.estimators`. 

I highly recommend you taking a look to understand the underlying code structure better and start Implementing your own estimators! 

Please do not hesitate to leave a message if you have any questions. 


## More Resources:

* [Key Features of Scikit Flow Illustrated](http://terrytangyuan.github.io/2016/03/14/scikit-flow-intro/)
* [High-level Learn Module in TensorFlow](http://terrytangyuan.github.io/2016/06/09/scikit-flow-v09/)
* [Introduction to Scikit Flow and why you want to start learning TensorFlow](https://medium.com/@ilblackdragon/tensorflow-tutorial-part-1-c559c63c0cb1)
* [DNNs, custom model and Digit recognition examples](https://medium.com/@ilblackdragon/tensorflow-tutorial-part-2-9ffe47049c92)
* [Categorical variables: One hot vs Distributed representation](https://medium.com/@ilblackdragon/tensorflow-tutorial-part-3-c5fc0662bc08)
* [Scikit Flow: Easy Deep Learning with TensorFlow and Scikit-learn](http://www.kdnuggets.com/2016/02/scikit-flow-easy-deep-learning-tensorflow-scikit-learn.html)

<p class="copyright text-muted">
  Copyright &copy; {{ site.title }} {{ site.time | date: '%Y' }}
</p>
<br><b>Banner Credit to TensorFlow Org</b>
