#!/usr/bin/env sh
./build/tools/convert_imageset \
--resize_height=180 \
--resize_width=240 \
./examples/viggynet/shoe_dataset/ \
./examples/viggynet/labels.txt \
./examples/viggynet/all
