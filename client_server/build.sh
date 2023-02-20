#!/bin/bash
# Build Go Code and add it to docker container

# Put installed packages into ./bin
export GOBIN=$PWD/`dirname $0`/bin
mkdir -p bin

env GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -trimpath -ldflags "$FLAGS" -v -o "bin/" ./cmd/...
