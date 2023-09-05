package main

import (
    "bufio"
    "context"
    "fmt"
    "os"
    "net/http"
    "strings"

    pb "golang.a2z.com/stableDiffusion/rpc"
)

func main() {
    reader := bufio.NewReader(os.Stdin)
    fmt.Print("Enter text: ")
    text, _ := reader.ReadString('\n')
    inputString := &pb.String{Text: text}

    // Create a client capable of talking to server
    // Copied from twitch
    client := pb.NewText2ImageProtobufClient("http://localhost:8080", &http.Client{})
    var (
        sd *pb.Bytes
        err error
    )

    sd, err = client.DiffusionModel(context.Background(), inputString)
    if err != nil {
        fmt.Println("Stable Diffusion Errored out")
    } else {
        // Write to file
        fname := strings.Replace(inputString.Text, " ", "_", -1)
        fname = fmt.Sprintf("%s.png", strings.Replace(fname, "\n","", -1))
        f, err := os.Create(fname)
        if err != nil {
            panic(err)
        } else {
            f.Write(sd.Bytes)
        }
    }
}
