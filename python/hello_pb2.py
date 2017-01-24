# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hello.proto',
  package='hello',
  syntax='proto3',
  serialized_pb=_b('\n\x0bhello.proto\x12\x05hello\"\r\n\x0bInfoRequest\"\x1c\n\tInfoReply\x12\x0f\n\x07message\x18\x01 \x01(\t28\n\x05Hello\x12/\n\x07GetInfo\x12\x12.hello.InfoRequest\x1a\x10.hello.InfoReplyb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_INFOREQUEST = _descriptor.Descriptor(
  name='InfoRequest',
  full_name='hello.InfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=35,
)


_INFOREPLY = _descriptor.Descriptor(
  name='InfoReply',
  full_name='hello.InfoReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='hello.InfoReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=65,
)

DESCRIPTOR.message_types_by_name['InfoRequest'] = _INFOREQUEST
DESCRIPTOR.message_types_by_name['InfoReply'] = _INFOREPLY

InfoRequest = _reflection.GeneratedProtocolMessageType('InfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _INFOREQUEST,
  __module__ = 'hello_pb2'
  # @@protoc_insertion_point(class_scope:hello.InfoRequest)
  ))
_sym_db.RegisterMessage(InfoRequest)

InfoReply = _reflection.GeneratedProtocolMessageType('InfoReply', (_message.Message,), dict(
  DESCRIPTOR = _INFOREPLY,
  __module__ = 'hello_pb2'
  # @@protoc_insertion_point(class_scope:hello.InfoReply)
  ))
_sym_db.RegisterMessage(InfoReply)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class HelloStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.GetInfo = channel.unary_unary(
          '/hello.Hello/GetInfo',
          request_serializer=InfoRequest.SerializeToString,
          response_deserializer=InfoReply.FromString,
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
            request_deserializer=InfoRequest.FromString,
            response_serializer=InfoReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'hello.Hello', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaHelloServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def GetInfo(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaHelloStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def GetInfo(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    GetInfo.future = None


  def beta_create_Hello_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('hello.Hello', 'GetInfo'): InfoRequest.FromString,
    }
    response_serializers = {
      ('hello.Hello', 'GetInfo'): InfoReply.SerializeToString,
    }
    method_implementations = {
      ('hello.Hello', 'GetInfo'): face_utilities.unary_unary_inline(servicer.GetInfo),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Hello_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('hello.Hello', 'GetInfo'): InfoRequest.SerializeToString,
    }
    response_deserializers = {
      ('hello.Hello', 'GetInfo'): InfoReply.FromString,
    }
    cardinalities = {
      'GetInfo': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'hello.Hello', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
