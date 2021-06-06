# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 21:16:28 2020

@author: mital
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import random

tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.FATAL)

print(tf.__version__)
mnist = input_data.read_data_sets("./MNIST_data/", one_hot=True)

# Training data 
tr_data = mnist.train.images
print("Training data shape: {0}".format(tr_data.shape)) # (55000, 784)

# Find 10 random images from training data and display them
# First find 10 random rows 
randIntList = [random.randrange(tr_data.shape[0]) for _ in range(10)]
fig1, fig1_axes = plt.subplots(ncols=10, nrows=1, constrained_layout=True)


img = np.reshape(tr_data[randIntList[3],:],[28,28])
fig1_axes[0].plot(plt.imshow(img,cmap = "gray"))

for i in range(len(randIntList)):
    img = np.reshape(tr_data[randIntList[i],:],[28,28])
    fig1_axes[i].plot(plt.imshow(img,cmap = "gray"))



