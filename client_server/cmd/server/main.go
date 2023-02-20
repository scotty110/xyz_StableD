package main

import (
    "context"
    "net/http"
    "fmt"
    "os"

    "golang.a2z.com/stableDiffusion/internal/hooks"
    pb "golang.a2z.com/stableDiffusion/rpc"
)


type diffusionServer struct{}


func (s *diffusionServer) DiffusionModel(ctx context.Context, req *pb.String) (*pb.Bytes, error) {
    client := pb.NewText2ImageProtobufClient("http://localhost:9001", &http.Client{}) 
    resp, err := client.DiffusionModel(context.Background(), req)
    if err == nil {
        fmt.Println("Got a reponce from Stable Diffusion Model")
    }
    return resp, err
}


func main() {
    hooks := hooks.LoggingHooks(os.Stderr) 
    twirpHandler := pb.NewText2ImageServer(&diffusionServer{}, hooks)

    mux := http.NewServeMux() //Can use any mux 
    mux.Handle(twirpHandler.PathPrefix(), twirpHandler)

    http.ListenAndServe(":8080", mux)
}
