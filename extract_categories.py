import pickle
import numpy as np

map = {}
for i in xrange(12):
    map[i] = []
counter = 0
with open('labels.txt') as file:
    for line in file:
        parts = line.split()
        id = int(parts[0][:-4])
        cat = int(parts[1])
        map[cat].append(id)
        counter += 1
    with open('cat_map.pickle', 'wb') as outfile:
        pickle.dump(map, outfile)
