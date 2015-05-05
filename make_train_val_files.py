import os
import random

root = "./examples/viggynet/shoe_dataset/"
train = []
val = []
for id in xrange(0, 11826):
	filename = root + str(id) + ".txt"
	with open(filename) as f:
		lines = [line.strip() for line in f]
		label = lines[5]
		entry = str(id) + ".jpg " + str(label) + "\n"
		if random.random() < 0.8:
			train.append(entry)
		else:
			val.append(entry)
with open(root + "trainfile", "wb") as trainfile:
	for t in train:
		trainfile.write(t)
with open(root + "valfile", "wb") as valfile:
	for v in val:
		valfile.write(v)
