# Stable Diffusion Stuff
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

import sys
import numpy as np

# Twirp Stuff
import asyncio
import logging

from twirp.context import Context
from twirp.asgi import TwirpASGIApp

import server_pb2
import server_twirp


class model():
    def __init__(self):
        #model_id = "CompVis/stable-diffusion-v1-4"
        model_id = "stabilityai/stable-diffusion-2-1"
        device = "cuda"

        pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, revision="fp16")
        self.pipe = pipe.to(device)
        self.pipe.enable_attention_slicing()

    def run(self, prompt:str):
        image = self.pipe( prompt ).images[0]
        return np.array(image, dtype=np.float64)


#class Text2Image(object):
class T2IService(object):
    def __init__(self):
        self.sd_model = model()

    def DiffusionModel(self, context, req) -> server_pb2.NumpyArray:
        array = self.sd_model.run( req.Text )
        print(array.shape)

        # Turn into PD array object
        pb_array = server_pb2.NumpyArray()
        pb_array.Array = array.tobytes()
        pb_array.Shape = (np.array(array.shape)).tobytes()

        return pb_array


#if __name__ == '__main__':
logging.basicConfig() 
#service = hello_twirp.HelloWorldServer(service=HelloService())
service = server_twirp.Text2ImageServer(service=T2IService())
app = TwirpASGIApp()
app.add_service(service)
    
print("Exit")
