import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import hello_pb2 as hello__pb2
import hello_pb2 as hello__pb2


class HelloStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetInfo = channel.unary_unary(
        '/hello.Hello/GetInfo',
        request_serializer=hello__pb2.InfoRequest.SerializeToString,
        response_deserializer=hello__pb2.InfoReply.FromString,
        )


class HelloServicer(object):

  def GetInfo(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_HelloServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetInfo,
          request_deserializer=hello__pb2.InfoRequest.FromString,
          response_serializer=hello__pb2.InfoReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'hello.Hello', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
