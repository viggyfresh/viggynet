import os
import random

label_index = 0
train = []
val = []
root = "./examples/viggynet/shoe_dataset"
root_dirs = os.listdir(root)
for root_d in root_dirs:
    if root_d == ".DS_Store":
        continue
    style_dirs = os.listdir(root + "/" + root_d)
    for style_d in style_dirs:
        if style_d == ".DS_Store":
            continue
        brand_dirs = os.listdir(root + "/" + root_d + "/" + style_d)
        for brand_d in brand_dirs:
            if brand_d == ".DS_Store":
                continue
            images = os.listdir(root + "/" + root_d + "/" + style_d + "/" + brand_d)
            for image in images:
                if image == ".DS_Store":
                    continue
                if random.random() < 0.8:
                    train.append(root_d + "/" + style_d + "/" + brand_d + "/" + image + " " + str(label_index) + "\n")
                else:
                    val.append(root_d + "/" + style_d + "/" + brand_d + "/" + image + " " + str(label_index) + "\n")
        label_index += 1
trainfile = open(root + "/trainfile", "wb")
for t in train:
    trainfile.write(t)
valfile = open(root + "/valfile", "wb")
for v in val:
    valfile.write(v)
