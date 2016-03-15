---
layout:     post
title:      "Introduction to Scikit Flow"
subtitle:   "A Simplified Interface to TensorFlow"
date:       2016-03-14
author:     "Yuan Tang"
header-img: "img/tensorflow-bg.jpg"
tags:
    - Deep Learning
    - TensorFlow
    - Scikit Flow
    - Technology
    - Open Source
---


# Deep Learning Models

## Deep Neural Network
Example of 3 layer deep neural network with 10, 20 and 10 hidden units respectively:

```python

import skflow
from sklearn import datasets, metrics

iris = datasets.load_iris()
classifier = skflow.TensorFlowDNNClassifier(hidden_units=[10, 20, 10], n_classes=3)
classifier.fit(iris.data, iris.target)
score = metrics.accuracy_score(iris.target, classifier.predict(iris.data))
print("Accuracy: %f" % score)
```

## Custom Model
Example of how to pass a custom model to the TensorFlowEstimator:

```python
import skflow
from sklearn import datasets, metrics

iris = datasets.load_iris()

def my_model(X, y):
    """This is DNN with 10, 20, 10 hidden layers, and dropout of 0.5 probability."""
    layers = skflow.ops.dnn(X, [10, 20, 10], keep_prob=0.5)
    return skflow.models.logistic_regression(layers, y)

classifier = skflow.TensorFlowEstimator(model_fn=my_model, n_classes=3)
classifier.fit(iris.data, iris.target)
score = metrics.accuracy_score(iris.target, classifier.predict(iris.data))
print("Accuracy: %f" % score)
```

## Recurrent Neural Network
* Various recurrent units, e.g. GRU, RNN, LSTM
* Bidirectional RNN
* Multi-layer RNN

```python
classifier = skflow.TensorFlowRNNClassifier(rnn_size=EMBEDDING_SIZE, 
    n_classes=15, cell_type='gru', input_op_fn=input_op_fn,
    num_layers=1, bidirectional=False, sequence_length=None,
    steps=1000, optimizer='Adam', learning_rate=0.01, continue_training=True)
```

## Convolutional Neural Network

```python
# Loading MNIST data
mnist = input_data.read_data_sets('MNIST_data')

def max_pool_2x2(tensor_in):
    return tf.nn.max_pool(tensor_in, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1],
        padding='SAME')

def conv_model(X, y):
    # reshape X to 4d tensor with 2nd and 3rd dimensions being image width and height
    # final dimension being the number of color channels
    X = tf.reshape(X, [-1, 28, 28, 1])
    # first conv layer will compute 32 features for each 5x5 patch
    with tf.variable_scope('conv_layer1'):
        h_conv1 = skflow.ops.conv2d(X, n_filters=32, filter_shape=[5, 5], 
                                    bias=True, activation=tf.nn.relu)
        h_pool1 = max_pool_2x2(h_conv1)
    # second conv layer will compute 64 features for each 5x5 patch
    with tf.variable_scope('conv_layer2'):
        h_conv2 = skflow.ops.conv2d(h_pool1, n_filters=64, filter_shape=[5, 5], 
                                    bias=True, activation=tf.nn.relu)
        h_pool2 = max_pool_2x2(h_conv2)
        # reshape tensor into a batch of vectors
        h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
    # densely connected layer with 1024 neurons
    h_fc1 = skflow.ops.dnn(h_pool2_flat, [1024], activation=tf.nn.relu, keep_prob=0.5)
    return skflow.models.logistic_regression(h_fc1, y)

# Training and predicting
classifier = skflow.TensorFlowEstimator(
    model_fn=conv_model, n_classes=10, batch_size=100, steps=20000,
    learning_rate=0.001)
```

# Modelling Techniques

## Early Stopping

```python
val_monitor = skflow.monitors.ValidationMonitor(X_val, y_val,
                                                early_stopping_rounds=200,
                                                n_classes=3)
# classifier with early stopping on validation data
classifier = skflow.TensorFlowDNNClassifier(hidden_units=[10, 20, 10],
                                             n_classes=3, steps=2000)
classifier.fit(X_train, y_train, val_monitor)
```

## Custom Decay Function for Learning Rate 

```python
# setup exponential decay function
def exp_decay(global_step):
    return tf.train.exponential_decay(
        learning_rate=0.1, global_step=global_step,
        decay_steps=100, decay_rate=0.001)

# use customized decay function in learning_rate
classifier = skflow.TensorFlowDNNClassifier(hidden_units=[10, 20, 10],
                                            n_classes=3, steps=800,
                                            learning_rate=exp_decay)
```



# Additional Features

## Monitors

```python
def conv_model(X, y):
    X = tf.expand_dims(X, 3)
    features = tf.reduce_max(skflow.ops.conv2d(X, 12, [3, 3]), [1, 2])
    features = tf.reshape(features, [-1, 12])
    return skflow.models.logistic_regression(features, y)

val_monitor = monitors.ValidationMonitor(X_val, y_val, n_classes=10, print_steps=50)
classifier = skflow.TensorFlowEstimator(model_fn=conv_model, n_classes=10,
                                        steps=1000, learning_rate=0.05,
                                        batch_size=128)
classifier.fit(X_train, y_train, val_monitor)
```

## Flexible Automatic Input Handling
* Numpy matrix/array
* Pandas
* Dask
* Iterators

Sometimes when your dataset is too large to hold in the memory you may want to load it into a out-of-core dataframe with the help of dask library to firstly draw sample batches and then load into memory for training. 


```python
# We can load data into pandas.DataFrame
X_train, y_train, X_test, y_test = [pd.DataFrame(data) for data in [X_train, y_train, X_test, y_test]]
# Or load data into dask.DataFrame, details see: http://dask.pydata.org/en/latest/dataframe.html
X_train, y_train, X_test, y_test = [dd.from_pandas(data, npartitions=2) for data in [X_train, y_train, X_test, y_test]]

classifier = skflow.TensorFlowLinearClassifier(n_classes=3)

classifier.fit(X_train, y_train)
# Make predictions on each partitions of testing data
predictions = X_test.map_partitions(classifier.predict).compute()
# Calculate accuracy
score = metrics.accuracy_score(y_test.compute(), predictions)
```


## Model Persistence

Each estimator has a ``save`` method which takes folder path where all model information will be saved. For restoring you can just call ``skflow.TensorFlowEstimator.restore(path)`` and it will return object of your class.

```python
classifier = skflow.TensorFlowLinearRegression()
classifier.fit(...)
classifier.save('/tmp/tf_examples/my_model_1/')

new_classifier = TensorFlowEstimator.restore('/tmp/tf_examples/my_model_2')
new_classifier.predict(...)
```

## Summaries/TensorBoard

To get nice visualizations and summaries you can use ``logdir`` parameter on ``fit``. It will start writing summaries for ``loss`` and histograms for variables in your model. You can also add custom summaries in your custom model function by calling ``tf.summary`` and passing Tensors to report.

```python
classifier = skflow.TensorFlowLinearRegression()
classifier.fit(X, y, logdir='/tmp/tf_examples/my_model_1/')
```

Then run next command in command line:

```bash
tensorboard --logdir=/tmp/tf_examples/my_model_1
```

and follow reported url.

<img class="shadow" width="1000" src="/img/text_classification_rnn_graph.png" />
<img class="shadow" width="1000" src="/img/text_classification_rnn_loss.png" />



Other Examples can be found on Github:

* Text classification (RNN & Convolution, word and character-level)
* Digits & MNIST (Conv, more Conv and ResNet)
* Language models
* Neural Translation Model





Copyright Reserved Yuan Tang 2016
