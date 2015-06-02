import numpy as np

model = 'vgg'
layer = 'fc8'
filename = 'features_' + model + '_' + layer + '.npy'
D = np.load(filename)

for i in xrange(0, 11826):
    feats = D[i]
    norm = np.linalg.norm(feats)
    D[i] = (feats / norm)
np.save('features_' + model + '_' + layer + '_norm', D)
