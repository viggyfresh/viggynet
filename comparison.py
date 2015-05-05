import os
import numpy as np
import sys
import caffe
import lmdb

TRIAL_NUM = 7
keys = []

lmdb_path = './examples/viggynet/all/'
lmdb_path2 = './examples/viggynet/features/'
env = lmdb.open(lmdb_path, readonly=True)
env2 = lmdb.open(lmdb_path2, readonly=True)
with env.begin() as txn:
    with txn.cursor() as cursor:
        cursor.first()
	key, val = cursor.item()
	key = key[key.find('_')+1:]
	keys.append(key)
	while cursor.next():
	    key, val = cursor.item()
	    key = key[key.find('_')+1:]
	    keys.append(key)

N_rd = len(keys)
D = []

def make_float_arr(datum):
    return np.array([fd for fd in datum.float_data])

# now let's just get the first image's features
with env2.begin() as txn:
    with txn.cursor() as cursor:
	for i in xrange(N_rd):
            key = str(i)
            val = cursor.get(key)
            datum = caffe.proto.caffe_pb2.Datum()
            datum.ParseFromString(val)
            D.append(make_float_arr(datum))
            
D = np.array(D)


result = D - D[TRIAL_NUM]
squared_dists  = np.square(result)
sum_squares = np.sum(squared_dists, axis=1)
dists = np.sqrt(sum_squares)
sorted_indices = np.argsort(dists)
closest = sorted_indices[:6]

print [keys[close] for close in closest]
