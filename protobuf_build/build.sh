#!/bin/bash

mkdir -p ./build/ha_vector/messaging > /dev/null
cp -fr ./prereqs/* ./build > /dev/null

rm -f ../ha_vector/messaging/*.py > /dev/null

pip install -r ../requirements.txt > /dev/null

python3 -m grpc_tools.protoc -I ./build --python_out ../ --grpc_python_out ../ ./build/ha_vector/messaging/*.proto
cp -f ./prereqs/*.py ../ha_vector/messaging > /dev/null
rm -rf ./build