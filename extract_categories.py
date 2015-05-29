import pickle
import numpy as np

cat_map = {}
rev_map = {}
for i in xrange(12):
    cat_map[i] = []
counter = 0
with open('labels.txt') as file:
    for line in file:
        parts = line.split()
        id = int(parts[0][:-4])
        cat = int(parts[1])
        cat_map[cat].append(id)
        rev_map[id] = cat
        counter += 1
    with open('cat_map.pickle', 'wb') as outfile:
        pickle.dump(cat_map, outfile)
    with open('rev_map.pickle', 'wb') as outfile:
        pickle.dump(rev_map, outfile)
