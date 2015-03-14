import os
import caffe
import lmdb
import numpy as np

lmdb_path = './examples/viggynet/features'
env = lmdb.open(lmdb_path, readonly=True)

N_rd = 1
D = []

def make_float_arr(datum):
    return np.array([fd for fd in datum.float_data])

# now let's just get the first image's features
with env.begin() as txn:
    with txn.cursor() as cursor:
	key = str(0)
	val = cursor.get(key)
        datum = caffe.proto.caffe_pb2.Datum()
        datum.ParseFromString(val)
	D.append(make_float_arr(datum))
            
D = np.array(D)
print D
