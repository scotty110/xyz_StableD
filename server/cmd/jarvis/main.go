package main

import (
    "context"
    "net/http"
    "fmt"

    pb "golang.a2z.com/jarvisServer/rpc"
)


type JarvisServer struct{}


func (s *JarvisServer) WhisperServer(ctx context.Context, req *pb.NumpyArray) (*pb.String, error) {
    client := pb.NewGetAudioProtobufClient("http://localhost:9001", &http.Client{}) // pb.?
    resp, err := client.WhisperEnd(context.Background(), req)
    if err == nil {
        fmt.Println("Got a reponce from whisper")
    }
}


func (s *JarvisServer) BloomServer(ctx context.Context, req *pb.String) (*pb.NumpyArray, error) {
    client := pb.NewGetEmbeddingProtobufClient("http://localhost:9002", &http.Client{}) // pb.?
    resp, err := client.BloomEnd(context.Background(), req)
    if err == nil {
        fmt.Println("Got a reponce from bloom")
    }
}


func (s *JarvisServer) DataBaseServer(ctx context.Context, req *pb.numpyArray) (*pb.Command, error) {
    client := pb.NewGetCommandProtobufClient("http://localhost:9003", &http.Client{}) // pb.?
    resp, err := client.DataBaseEnd(context.Background(), req)
    if err == nil {
        fmt.Println("Got a reponce from Data Base")
    }
}



func main() {
    twirpHandler := pbs.server(&JarvisServer)
    mux := http.NewServeMux() //Can use any mux 
    mux.Handle(twirpHandler.PathPrefix(), twirpHandler)

    fmt.Println("HERE")
    http.ListenAndServe(":8080", mux)
}
