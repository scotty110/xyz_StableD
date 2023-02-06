#!/bin/bash
protoc -I ../server/rpc/ --python_out=./ --twirpy_out=./ ../server/rpc/server.proto
