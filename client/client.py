'''
https://github.com/verloop/twirpy
'''
import asyncio
import logging

from twirp.context import Context
from twirp.exceptions import TwirpServerException

import server_pb2
import server_twirp

import numpy as np

def deserialize(m:server_pb2.NumpyArray) -> np.array:                                   
    shape_array = (np.frombuffer(m.Shape, dtype=np.int64))                      
    value_array = np.reshape(np.frombuffer(m.Array, dtype=np.int64), newshape=shape_array)
    return value_array


def run() -> None:
    client = server_twirp.Text2ImageClient("http://localhost:9001", timeout=40)
    client = server_twirp.Text2ImageClient("http://localhost:8080", timeout=40)

    # if you are using a custom prefix, then pass it as `server_path_prefix`
    # param to `MakeHat` class.
    try:
        response = client.DiffusionModel(ctx=Context(), request=server_pb2.String(Text='cartoon sail boat in the ocean'))
        np_array = deserialize(response)     
        print( np_array.shape )
    except TwirpServerException as e:
        print(e.code, e.message, e.meta, e.to_dict())


if __name__ == '__main__':
    logging.basicConfig()
    #asyncio.run(run())
    run()
