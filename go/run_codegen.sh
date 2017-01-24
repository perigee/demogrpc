#!/bin/bash

protoc -I ../protoc ../protoc/hello.proto  --go_out=plugins=grpc:pb
