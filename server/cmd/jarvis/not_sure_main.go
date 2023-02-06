package not_sure_main

import (
    "context"
    "net/http"
    "fmt"

    pbs "golang.a2z.com/jarvisServer/rpc/server"
    //pbs "golang.a2z.com/jarvisServer/rpc/server"
    //pbc "golang.a2z.com/jarvisServer/rpc/client"
)


type JarvisServer struct{}


func (s *JarvisServer) Whisper(ctx context.Context, req *pbs.numpyArray) (*pbs.NumpyArray, error) {
    //TODO
    client := pbc.Whisper(context.Background(), &pbs
}


func (s *JarvisServer) Bloom(ctx context.Context, req *pbs.numpyArray) (*pbs.NumpyArray, error) {
    //TODO
}


func (s *JarvisServer) DataBase(ctx context.Context, req *pbc.numpyArray) (*pbc.Command, error) {
    //TODO
}



func main() {
    twirpHandler := pbs.server(&JarvisServer)
    mux := http.NewServeMux() //Can use any mux 
    mux.Handle(twirpHandler.PathPrefix(), twirpHandler)

    fmt.Println("HERE")
    http.ListenAndServe(":8080", mux)
    // TODO
}
