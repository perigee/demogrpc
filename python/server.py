from concurrent import futures
import time
import grpc
import hello_pb2
import hello_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(hello_pb2_grpc.HelloServicer):

    def GetInfo(self, request, context):
        return hello_pb2.InfoReply(message="hello")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_HelloServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:3000')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
 
if __name__ == '__main__':
    serve()
