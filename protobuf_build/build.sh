#!/bin/bash

mkdir -p ./build/ha_vector/messaging > /dev/null
cp -fr ./prereqs/* ./build > /dev/null
# cp -f ../ha_vector/messaging/*.proto ./build/ha_vector/messaging > /dev/null
rm -f ../ha_vector/messaging/* > /dev/null
pip install -r ../requirements.txt > /dev/null
python3 -m grpc_tools.protoc -I ./build --python_out ../ha_vector/messaging --grpc_python_out ../ha_vector/messaging ./build/ha_vector/messaging/*.proto
rm -rf ./build