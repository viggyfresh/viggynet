#!/usr/bin/env sh
# Compute the mean image from the imagenet training leveldb
# N.B. this is available in data/ilsvrc12

./build/tools/compute_image_mean examples/viggynet/shoes_train_lmdb \
  examples/viggynet/shoes_mean.binaryproto

echo "Done."
