package main

import (
	"log"

	context "golang.org/x/net/context"

	"google.golang.org/grpc"

	pb "github.com/perigee/demogrpc/go/pb"
)

const (
	address = "localhost:3000"
)

func main() {
	conn, err := grpc.Dial(address, grpc.WithInsecure())
	if err != nil {
		log.Fatalf("Cannot connect: %v", err)
	}
	defer conn.Close()

	c := pb.NewHelloClient(conn)

	r, err := c.GetInfo(context.Background(), &pb.InfoRequest{})
	if err != nil {
		log.Fatalf("Cannot get info: %v", err)
	}

	log.Printf("Server: %s", r.Message)
}
