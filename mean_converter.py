import caffe
import numpy as np

blob = caffe.proto.caffe_pb2.BlobProto()
data = open('shoes_mean.binaryproto', 'rb').read()
blob.ParseFromString(data)
arr = np.array(caffe.io.blobproto_to_array(blob))
np.save('shoes_mean', arr[0])
