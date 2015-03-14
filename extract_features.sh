#!/usr/bin/env sh

./build/tools/extract_features.bin \
./examples/viggynet/vgg.caffemodel \
./examples/viggynet/vgg.prototxt \
fc6 \
./examples/viggynet/features \
237 \
lmdb \
GPU
