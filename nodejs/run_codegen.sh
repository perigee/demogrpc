#!/bin/bash
./protoc -I ../protoc  ../protoc/hello.proto --js_out=import_style=commonjs,binary:. --grpc_out=. --plugin=protoc-gen-grpc=/opt/app/node_modules/grpc-tools/bin/protoc_plugin.js
