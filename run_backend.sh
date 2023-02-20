#!/bin/bash
# Run servers 

eval "$(conda shell.bash hook)" 
conda activate stabled 

# Start Stable Diffusion model
cd ./stable_diffusion 
nohup sh ./run.sh  >/dev/null 2>&1 &

# Start Twip server
#echo $PWD 
cd ../client_server/bin 
nohup ./server >/dev/null 2>&1 &
