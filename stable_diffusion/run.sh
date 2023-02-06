#!/bin/bash

uvicorn main:app --timeout-keep-alive 60 --port 9001 
#uvicorn server:app --port 8080 
