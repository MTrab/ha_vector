#!/bin/bash

mkdir ./build > /dev/null
cp -fr ./prereqs/* ./build > /dev/null
cp -f ../ha_vector/messaging/*.proto ./build > /dev/null
rm -f ../ha_vector/messaging/*.py > /dev/null
pip install -r ../requirements.txt > /dev/null
python3 -m grpc_tools.protoc -I ./build --python_out ../ha_vector/messaging --grpc_python_out ../ha_vector/messaging ./build/*.proto
rm -rf ./build