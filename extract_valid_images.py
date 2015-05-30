import numpy as np
import caffe
import pickle

caffe.set_mode_cpu()
all_ids = []

for i in xrange(0, 11826):
    print i
    try:
        img = caffe.io.load_image('shoe_dataset/' + str(i) + '.jpg')
        all_ids.append(i)
    except:
        continue
output = np.array(all_ids)
np.save('valid_images', output)
