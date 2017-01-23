from __future__ import print_function

import grpc

import hello_pb2
import hello_pb2_grpc


def run():
  channel = grpc.insecure_channel('localhost:3000')
  stub = hello_pb2_grpc.HelloStub(channel)
  response = stub.GetInfo(hello_pb2.InfoRequest())
  print("Greeter client received: " + response.message)


if __name__ == '__main__':
  run()
