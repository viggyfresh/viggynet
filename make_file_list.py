import os

root = "./examples/viggynet/"

with open(root + "images.txt", 'wb') as f:
    data_dir = os.listdir(root + "shoe_dataset")
    for data in data_dir:
        if data.endswith(".jpg"):
	    f.write(root + "shoe_dataset/" + data + "\n")
