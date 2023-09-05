# Stable Diffusion with RPC Calls
Run Stable diffusion as an RPC server, provide access with a command line utility

## Server
Due to wanting to experiment with routing requests, and provide future expandability,
2 servers exist: a stable diffusion server, and a "request" server

### Stable Diffusion
This RPC server runs the AI model. It takes in a protobuf `String` message and 
runs a stable diffusion model with the text promt and returns a `Bytes` message 
containing the bytes of the output of the AI model in PNG format.

### Requests
This is a simple Twirp server that acts as a middleman between the client and the
AI model. It is a simple message passing interface. The idea is that it could 
route messages to multiple models if needed. 

## Client
Client currently runs on the localhost were the servers are running. It will prompt
a user for some input text, and save the image that is returned from the AI model.



