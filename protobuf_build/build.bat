@echo off

mkdir ./build
copy /Y ./prereqs/*.* ./build
copy /Y ../ha_vector/messaging/*.proto ./build
del /F /Q ../ha_vector/messaging/*.py

python3 -m grpc_tools.protoc -I ./build --python_out ../ha_vector/messaging --grpc_python_out ../ha_vector/messaging ./build/*.proto

rmdir /S /Q ./build