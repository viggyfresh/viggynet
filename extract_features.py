import numpy as np
import caffe

caffe.set_mode_cpu()
net = caffe.Net('vgg.prototxt', 'vgg.caffemodel', caffe.TEST)

transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2,0,1))
transformer.set_raw_scale('data', 255)
net.blobs['data'].reshape(1, 3, 224, 224)

D = np.zeros((11827, 4096))

for i in xrange(0, 11826):
    print i
    try:
        img = caffe.io.load_image('shoe_dataset/' + str(i) + '.jpg')
        net.blobs['data'].data[...] = transformer.preprocess('data', img)
        out = net.forward()
        feats = net.blobs['fc6'].data.reshape((4096,))
        D[i] = feats
        rev = net.backward()
    except:
        feats = -9999 * np.ones((4096,))
        D[i] = feats
        continue

np.save('features', D)
