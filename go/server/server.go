package main

import (
	"log"

	context "golang.org/x/net/context"

	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"

	"net"

	pb "github.com/perigee/demogrpc/go/pb"
)

const (
	port = ":3000"
)

type server struct{}

func (s *server) GetInfo(ctx context.Context, in *pb.InfoRequest) (*pb.InfoReply, error) {
	return &pb.InfoReply{Message: "Hello from go"}, nil
}

func main() {
	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("Cannot Listen %v", err)
	}

	s := grpc.NewServer()
	pb.RegisterHelloServer(s, &server{})

	reflection.Register(s)
	if err := s.Serve(lis); err != nil {
		log.Fatalf("Failed to serve: %v", err)
	}
}
