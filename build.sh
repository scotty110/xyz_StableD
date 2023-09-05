#!/bin/bash
# Build project 

# Setup Env
#mkdir -p bin

# Build Twirp Servers first
cd client_server
sh ./build.sh

#cp ./bin/client ../bin/ 
#cp ./bin/server ../bin/ 
