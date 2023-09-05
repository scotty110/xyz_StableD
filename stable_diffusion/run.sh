#!/bin/bash
# Run stable diff model

eval "$(conda shell.bash hook)"                                           
conda activate stabled 

uvicorn main:app --timeout-keep-alive 60 --port 9001 
