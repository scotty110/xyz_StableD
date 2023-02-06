package main

import (
    "context"
    "net/http"
    "fmt"

    pb "golang.a2z.com/server/rpc"
)


type DiffusionServer struct{}


func (s *DiffusionServer) GetImage(ctx context.Context, req *pb.String) (*pb.NumpyArray, error) {
    client := pb.NewGetAudioProtobufClient("http://localhost:9001", &http.Client{}) 
    resp, err := client.DiffusionModel(context.Background(), req)
    if err == nil {
        fmt.Println("Got a reponce from Stable Diffusion Model")
    }
}


func main() {
    twirpHandler := pbs.server(&JarvisServer)
    mux := http.NewServeMux() //Can use any mux 
    mux.Handle(twirpHandler.PathPrefix(), twirpHandler)

    fmt.Println("HERE")
    http.ListenAndServe(":8080", mux)
}
