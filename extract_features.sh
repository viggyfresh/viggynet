#!/usr/bin/env sh

./build/tools/extract_features.bin \
./examples/viggynet/snapshot_iter_2000.caffemodel \
./examples/viggynet/shoes_feature_extract.prototxt \
fc1 \
./examples/viggynet/features \
237 \
lmdb \
GPU
