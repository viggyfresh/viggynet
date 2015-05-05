import os
import numpy as np
import sys
import caffe
import lmdb

TRIAL_NUM = 0
keys = []

feats = np.load('features.npy')

result = feats - feats[TRIAL_NUM]
squared_dists  = np.square(result)
sum_squares = np.sum(squared_dists, axis=1)
dists = np.sqrt(sum_squares)
sorted_indices = np.argsort(dists)
closest = sorted_indices[:11]

print [i for i in closest]
