root = "./examples/viggynet/shoe_dataset/"

with open("./examples/viggynet/labels.txt", 'wb') as labels:
    for id in xrange(0, 11826):
	filename = root + str(id) + ".txt"
	with open(filename) as f:
		lines = [line.strip() for line in f]
		label = lines[5]
		entry = str(id) + ".jpg " + str(label) + "\n"
		labels.write(entry)
		
