# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arg_services/mining/v1beta/mining.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from arg_services.graph.v1 import graph_pb2 as arg__services_dot_graph_dot_v1_dot_graph__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='arg_services/mining/v1beta/mining.proto',
  package='arg_services.mining.v1beta',
  syntax='proto3',
  serialized_options=b'\n\036com.arg_services.mining.v1betaB\013MiningProtoP\001\242\002\003AMX\252\002\031ArgServices.Mining.V1beta\312\002\031ArgServices\\Mining\\V1beta\342\002%ArgServices\\Mining\\V1beta\\GPBMetadata\352\002\033ArgServices::Mining::V1beta',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'arg_services/mining/v1beta/mining.proto\x12\x1a\x61rg_services.mining.v1beta\x1a!arg_services/graph/v1/graph.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\"[\n\x12RunPipelineRequest\x12\x14\n\x05texts\x18\x01 \x03(\tR\x05texts\x12/\n\x06\x65xtras\x18\x0f \x01(\x0b\x32\x17.google.protobuf.StructR\x06\x65xtras\"|\n\x13RunPipelineResponse\x12\x34\n\x06graphs\x18\x01 \x03(\x0b\x32\x1c.arg_services.graph.v1.GraphR\x06graphs\x12/\n\x06\x65xtras\x18\x0f \x01(\x0b\x32\x17.google.protobuf.StructR\x06\x65xtras2\xa8\x01\n\rMiningService\x12\x96\x01\n\x0bRunPipeline\x12..arg_services.mining.v1beta.RunPipelineRequest\x1a/.arg_services.mining.v1beta.RunPipelineResponse\"&\x82\xd3\xe4\x93\x02 :\x01*\"\x1b/mining/v1beta/run_pipelineB\xb3\x01\n\x1e\x63om.arg_services.mining.v1betaB\x0bMiningProtoP\x01\xa2\x02\x03\x41MX\xaa\x02\x19\x41rgServices.Mining.V1beta\xca\x02\x19\x41rgServices\\Mining\\V1beta\xe2\x02%ArgServices\\Mining\\V1beta\\GPBMetadata\xea\x02\x1b\x41rgServices::Mining::V1betab\x06proto3'
  ,
  dependencies=[arg__services_dot_graph_dot_v1_dot_graph__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_RUNPIPELINEREQUEST = _descriptor.Descriptor(
  name='RunPipelineRequest',
  full_name='arg_services.mining.v1beta.RunPipelineRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='texts', full_name='arg_services.mining.v1beta.RunPipelineRequest.texts', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='texts', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extras', full_name='arg_services.mining.v1beta.RunPipelineRequest.extras', index=1,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='extras', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=166,
  serialized_end=257,
)


_RUNPIPELINERESPONSE = _descriptor.Descriptor(
  name='RunPipelineResponse',
  full_name='arg_services.mining.v1beta.RunPipelineResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='graphs', full_name='arg_services.mining.v1beta.RunPipelineResponse.graphs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='graphs', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extras', full_name='arg_services.mining.v1beta.RunPipelineResponse.extras', index=1,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='extras', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=259,
  serialized_end=383,
)

_RUNPIPELINEREQUEST.fields_by_name['extras'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_RUNPIPELINERESPONSE.fields_by_name['graphs'].message_type = arg__services_dot_graph_dot_v1_dot_graph__pb2._GRAPH
_RUNPIPELINERESPONSE.fields_by_name['extras'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['RunPipelineRequest'] = _RUNPIPELINEREQUEST
DESCRIPTOR.message_types_by_name['RunPipelineResponse'] = _RUNPIPELINERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RunPipelineRequest = _reflection.GeneratedProtocolMessageType('RunPipelineRequest', (_message.Message,), {
  'DESCRIPTOR' : _RUNPIPELINEREQUEST,
  '__module__' : 'arg_services.mining.v1beta.mining_pb2'
  # @@protoc_insertion_point(class_scope:arg_services.mining.v1beta.RunPipelineRequest)
  })
_sym_db.RegisterMessage(RunPipelineRequest)

RunPipelineResponse = _reflection.GeneratedProtocolMessageType('RunPipelineResponse', (_message.Message,), {
  'DESCRIPTOR' : _RUNPIPELINERESPONSE,
  '__module__' : 'arg_services.mining.v1beta.mining_pb2'
  # @@protoc_insertion_point(class_scope:arg_services.mining.v1beta.RunPipelineResponse)
  })
_sym_db.RegisterMessage(RunPipelineResponse)


DESCRIPTOR._options = None

_MININGSERVICE = _descriptor.ServiceDescriptor(
  name='MiningService',
  full_name='arg_services.mining.v1beta.MiningService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=386,
  serialized_end=554,
  methods=[
  _descriptor.MethodDescriptor(
    name='RunPipeline',
    full_name='arg_services.mining.v1beta.MiningService.RunPipeline',
    index=0,
    containing_service=None,
    input_type=_RUNPIPELINEREQUEST,
    output_type=_RUNPIPELINERESPONSE,
    serialized_options=b'\202\323\344\223\002 :\001*\"\033/mining/v1beta/run_pipeline',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MININGSERVICE)

DESCRIPTOR.services_by_name['MiningService'] = _MININGSERVICE

# @@protoc_insertion_point(module_scope)
