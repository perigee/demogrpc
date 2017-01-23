from grpc.tools import protoc

protoc.main(
    (
        '',
        '-I../protoc',
        '--python_out=.',
        '--grpc_python_out=.',
        '../protoc/hello.proto'
    )
)
