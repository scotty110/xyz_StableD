# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cserver.proto\x12\x0ctwirp.server\"*\n\nNumpyArray\x12\r\n\x05Shape\x18\x01 \x01(\x0c\x12\r\n\x05\x41rray\x18\x02 \x01(\x0c\"$\n\x05\x42ytes\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\r\n\x05\x42ytes\x18\x02 \x01(\x0c\"\x16\n\x06String\x12\x0c\n\x04Text\x18\x01 \x01(\t2I\n\nText2Image\x12;\n\x0e\x44iffusionModel\x12\x14.twirp.server.String\x1a\x13.twirp.server.BytesB\x14Z\x12./;diffusionServerb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'server_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\022./;diffusionServer'
  _NUMPYARRAY._serialized_start=30
  _NUMPYARRAY._serialized_end=72
  _BYTES._serialized_start=74
  _BYTES._serialized_end=110
  _STRING._serialized_start=112
  _STRING._serialized_end=134
  _TEXT2IMAGE._serialized_start=136
  _TEXT2IMAGE._serialized_end=209
# @@protoc_insertion_point(module_scope)