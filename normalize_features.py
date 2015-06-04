import numpy as np

model = 'alexnet'
layer = 'fc7'
filename = 'features_' + model + '_' + layer + '.npy'
D = np.load(filename)

for i in xrange(0, 11826):
    feats = D[i]
    if feats[0] != -9999 and feats[0] != -99999:
        norm = np.linalg.norm(feats)
        D[i] = (feats / norm)
np.save('features_' + model + '_' + layer + '_norm', D)
