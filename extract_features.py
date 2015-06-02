import numpy as np
import caffe

model = 'vgg'
width = 224
height = 224
dim = 1000
layer = 'fc8'

caffe.set_mode_cpu()
net = caffe.Net(model + '.prototxt', model + '.caffemodel', caffe.TEST)

transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2,0,1))
transformer.set_raw_scale('data', 255)
net.blobs['data'].reshape(1, 3, width, height)

D = np.zeros((11826, dim))

for i in xrange(0, 11826):
    print i
    try:
        img = caffe.io.load_image('shoe_dataset/' + str(i) + '.jpg')
        net.blobs['data'].data[...] = transformer.preprocess('data', img)
        out = net.forward()
        feats = net.blobs[layer].data.reshape((dim,))
        D[i] = feats
        rev = net.backward()
    except:
        feats = -99999 * np.ones((dim,))
        D[i] = feats
        continue

np.save('features_' + model + '_' + layer, D)
