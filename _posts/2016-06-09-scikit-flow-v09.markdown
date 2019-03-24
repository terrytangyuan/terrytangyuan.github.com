---
layout:     post
title:      "High-level Learn Module in TensorFlow"
subtitle:   "Seemless Integration and Changes on Scikit Flow"
date:       2016-06-09
author:     "Yuan Tang"
header-img: "img/inblog/tensorflow-bg.jpg"
tags:
    - Deep Learning
    - TensorFlow
    - Open Source
    - Machine Learning
    - Python
--- 

(This blog is featured in DataScienceWeekly [here](http://us3.campaign-archive2.com/?u=71a2b2a38789d4d25b738462f&id=ad8783e5dc&e=33631457e6))

Since Scikit Flow has been included in [v0.8](https://github.com/tensorflow/tensorflow/releases/tag/v0.8.0rc0) as its [TensorFlow Learn module](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/learn/python/learn), it has been under rapid development both internally and externally to push it towards distributed and work more seemlessly with TensorFlow's internals. As mentioned in its recent release [v0.9](https://github.com/tensorflow/tensorflow/releases/tag/v0.9.0rc0), it now works nicely with its other high-level internal modules, such as `contrib.layers`, `contrib.losses`, and `contrib.metrics`. There are many exciting changes since my [last post on introduction to Scikit Flow](http://terrytangyuan.github.io/2016/03/14/scikit-flow-intro/). 

In this post, I will explain some major changes introduced since [v0.9](https://github.com/tensorflow/tensorflow/releases/tag/v0.9.0rc0) to help existing users understand the code better as well as a call for contributors for this exciting and rapid growing project. To share some of my passion towards building and contributing open-source softwares, please take a look at this [interview blog](http://uptake.com/5-questions-with-uptake-data-scientist-and-scikit-flow-co-creator-yuan-tang/) from my company. 


## Distributed Estimator

With the great addition of [graph_actions module](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/learn/python/learn/graph_actions.py) that handles most of the complicated distributed logics of model training and evaluation, the [estimators](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/learn/python/learn/estimators) now incorporates `Supervisor` and `Coordinator` logics to train models in a distributed fasion. `Estimator` now accepts custom model function that accepts various signatures, such as the following:

* `(features, targets) -> (predictions, loss, train_op)`
* `(features, targets, mode) -> (predictions, loss, train_op)`
* `(features, targets, mode, params) -> (predictions, loss, train_op)`

Basically `train_op` can be specified instead of using `learn.trainer` internally so users are able to specify more customized things and a lot of high-levels in `contrib` folder can be utilized as well. You can inherit from basic estimator and build your own estimators that suit your needs without worrying about implementation details on communications between different threads and setting up a master supervisor. Please see the documentation for `Estimator` for most updated docs. You can find the work-in-progress API guides [here](https://www.tensorflow.org/versions/master/api_docs/python/contrib.learn.html). We haven't updated the examples yet but you can find a lot of unit tests that serve as most recent examples.

## Customized Model

For example, you can now build higly customized models like the following:

```python
from sklearn import datasets, metrics, cross_validation
import tensorflow as tf
from tensorflow.contrib import layers
from tensorflow.contrib import learn

def my_model(features, target):
  target = tf.one_hot(target, 3, 1, 0)
  features = layers.stack(features, layers.fully_connected, [10, 20, 10])
  prediction, loss = (
      tf.contrib.learn.models.logistic_regression_zero_init(features, target)
  )
  train_op = tf.contrib.layers.optimize_loss(
      loss, tf.contrib.framework.get_global_step(), optimizer='Adagrad',
      learning_rate=0.1)
  return {'class': tf.argmax(prediction, 1), 'prob': prediction}, loss, train_op

iris = datasets.load_iris()
x_train, x_test, y_train, y_test = cross_validation.train_test_split(
  iris.data, iris.target, test_size=0.2, random_state=35)

classifier = learn.Estimator(model_fn=my_model)
classifier.fit(x_train, y_train, steps=700)

predictions = classifier.predict(x_test)
```

To explain some details, you can now utilize high-level APIs in `contrib.layers` to `stack`various `fully_connected` layers with different layer specifications, such as number of hidden units, together with `contrib.layers.optimize_loss` to provide appropriate and highly flexible optimization details for your custom model. To have a quick glance at [`contrib.layers`](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/layers), you can see many commonly used layers such as `batch_norm`, `convolution2d`, `dropout`, and `fully_connected`, etc. Different optimizers, regularizers, can also be used. Note that `learn.ops` will be moved to `contrib.layers` and all these high-level APIs in contrib will be moved to TensorFlow core python module at some point in the future.

You can also provide a customized learning rate function such as exponential learning rate decay and specify that by providing a custom optimizer as shown below. 

```python
# setup exponential decay function
def exp_decay(global_step):
    return tf.train.exponential_decay(
        learning_rate=0.1, global_step=global_step,
        decay_steps=100, decay_rate=0.001)

# use customized decay function in learning_rate
optimizer = tf.train.AdagradOptimizer(learning_rate=exp_decay)
classifier = tf.contrib.learn.DNNClassifier(hidden_units=[10, 20, 10],
                                            n_classes=3,
                                            optimizer=optimizer)
```

## TensorFlow DataFrame

Similar to libraries like Pandas, a high-level [DataFrame module](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/learn/python/learn/dataframe) was included in TensorFlow Learn to facilitate many common data reading/parsing tasks from various resources such as `tensorflow.Examples`, `pandas.DataFrame`, etc. It also includes functions like `FeedingQueueRunner` to fetch data batches and put them in a queue so training and data feeding can now be performed at the same time in different threads to avoid wasting a lot of time waiting for data batchs to get fetched. Old `data_feeder` module will be deprecated soon. Again, if you are interested, please take a look at the unit tests for DataFrame that also serve as most recent examples. 


## Monitors

Major refactoring and enhancements have been added to monitors as well. You can now provide multiple highly customized monitors to perform different types of monitoring for things like validation, debugging, and unit testing. When you `fit()` the model, you can append a list of monitors to observe the training process. 

```python
estimator = tf.contrib.learn.Estimator(model_fn=linear_model_fn)
estimator.fit(input_fn=boston_input_fn, steps=21, 
        monitors=[ValidationMonitor(), DebuggingMonitor()])
```



## More Resources:

* [Key Features of Scikit Flow Illustrated](http://terrytangyuan.github.io/2016/03/14/scikit-flow-intro/)
* [Building Machine Learning Estimator in TensorFlow](http://terrytangyuan.github.io/2016/07/08/understand-and-build-tensorflow-estimator/)
* [Introduction to Scikit Flow and why you want to start learning TensorFlow](https://medium.com/@ilblackdragon/tensorflow-tutorial-part-1-c559c63c0cb1)
* [DNNs, custom model and Digit recognition examples](https://medium.com/@ilblackdragon/tensorflow-tutorial-part-2-9ffe47049c92)
* [Categorical variables: One hot vs Distributed representation](https://medium.com/@ilblackdragon/tensorflow-tutorial-part-3-c5fc0662bc08)
* [Scikit Flow: Easy Deep Learning with TensorFlow and Scikit-learn](http://www.kdnuggets.com/2016/02/scikit-flow-easy-deep-learning-tensorflow-scikit-learn.html)


Note: a work-in-progress documentation page can be found [here](https://www.tensorflow.org/versions/master/api_docs/python/contrib.learn.html). 

We welcome any contributions to this exciting project. No matter if it's simple typos, bug fixes/reports, or suggestions on enhancements and future directions. Do not hesitate to ask me if you'd like to see certain things in my future blogs. 

<p class="copyright text-muted">
  Copyright &copy; {{ site.title }} {{ site.time | date: '%Y' }}
</p>
<br><b>Banner Credit to TensorFlow Org</b>
