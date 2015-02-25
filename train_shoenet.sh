#!/usr/bin/env sh

./build/tools/caffe train \
    --solver=./examples/viggynet/shoes_solver.prototxt
