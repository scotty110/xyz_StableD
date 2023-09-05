# Stable Diffusion Stuff
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

import sys
import numpy as np
import io

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
        with io.BytesIO() as img_bytes:
            image.save(img_bytes, format="PNG")
            contents = img_bytes.getvalue()
        return contents


#class Text2Image(object):
class T2IService(object):
    def __init__(self):
        self.sd_model = model()

    def DiffusionModel(self, context, req) -> server_pb2.Bytes:
        bts = self.sd_model.run( req.Text )

        b_obj = server_pb2.Bytes()
        b_obj.Name = req.Text
        b_obj.Bytes = bts
        return b_obj
        


#if __name__ == '__main__':
logging.basicConfig() 
service = server_twirp.Text2ImageServer(service=T2IService())
app = TwirpASGIApp()
app.add_service(service)
    
print("Exit")
