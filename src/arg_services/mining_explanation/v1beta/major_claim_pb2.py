# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arg_services/mining_explanation/v1beta/major_claim.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='arg_services/mining_explanation/v1beta/major_claim.proto',
  package='arg_services.mining_explanation.v1beta',
  syntax='proto3',
  serialized_options=b'\n*com.arg_services.mining_explanation.v1betaB\017MajorClaimProtoP\001\242\002\003AMX\252\002$ArgServices.MiningExplanation.V1beta\312\002$ArgServices\\MiningExplanation\\V1beta\342\0020ArgServices\\MiningExplanation\\V1beta\\GPBMetadata\352\002&ArgServices::MiningExplanation::V1beta',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n8arg_services/mining_explanation/v1beta/major_claim.proto\x12&arg_services.mining_explanation.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x83\x01\n\x11MajorClaimRequest\x12\x1a\n\x08language\x18\x01 \x01(\tR\x08language\x12!\n\x0cmajor_claims\x18\x02 \x03(\tR\x0bmajorClaims\x12/\n\x06\x65xtras\x18\x0f \x01(\x0b\x32\x17.google.protobuf.StructR\x06\x65xtras\"\xa2\x01\n\x12MajorClaimResponse\x12[\n\x0cmajor_claims\x18\x01 \x03(\x0b\x32\x38.arg_services.mining_explanation.v1beta.MajorClaimResultR\x0bmajorClaims\x12/\n\x06\x65xtras\x18\x0f \x01(\x0b\x32\x17.google.protobuf.StructR\x06\x65xtras\"\xdf\x01\n\x10MajorClaimResult\x12n\n\x0csimilarities\x18\x01 \x03(\x0b\x32J.arg_services.mining_explanation.v1beta.MajorClaimResult.SimilaritiesEntryR\x0csimilarities\x12\x1a\n\x08keywords\x18\x02 \x03(\x08R\x08keywords\x1a?\n\x11SimilaritiesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x01R\x05value:\x02\x38\x01\x32\xc0\x01\n\x1cMajorClaimExplanationService\x12\x9f\x01\n\nMajorClaim\x12\x39.arg_services.mining_explanation.v1beta.MajorClaimRequest\x1a:.arg_services.mining_explanation.v1beta.MajorClaimResponse\"\x1a\x82\xd3\xe4\x93\x02\x14:\x01*\"\x0f/nlp/v1/vectorsB\xef\x01\n*com.arg_services.mining_explanation.v1betaB\x0fMajorClaimProtoP\x01\xa2\x02\x03\x41MX\xaa\x02$ArgServices.MiningExplanation.V1beta\xca\x02$ArgServices\\MiningExplanation\\V1beta\xe2\x02\x30\x41rgServices\\MiningExplanation\\V1beta\\GPBMetadata\xea\x02&ArgServices::MiningExplanation::V1betab\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_MAJORCLAIMREQUEST = _descriptor.Descriptor(
  name='MajorClaimRequest',
  full_name='arg_services.mining_explanation.v1beta.MajorClaimRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='language', full_name='arg_services.mining_explanation.v1beta.MajorClaimRequest.language', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='language', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='major_claims', full_name='arg_services.mining_explanation.v1beta.MajorClaimRequest.major_claims', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='majorClaims', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extras', full_name='arg_services.mining_explanation.v1beta.MajorClaimRequest.extras', index=2,
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
  serialized_start=161,
  serialized_end=292,
)


_MAJORCLAIMRESPONSE = _descriptor.Descriptor(
  name='MajorClaimResponse',
  full_name='arg_services.mining_explanation.v1beta.MajorClaimResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='major_claims', full_name='arg_services.mining_explanation.v1beta.MajorClaimResponse.major_claims', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='majorClaims', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extras', full_name='arg_services.mining_explanation.v1beta.MajorClaimResponse.extras', index=1,
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
  serialized_start=295,
  serialized_end=457,
)


_MAJORCLAIMRESULT_SIMILARITIESENTRY = _descriptor.Descriptor(
  name='SimilaritiesEntry',
  full_name='arg_services.mining_explanation.v1beta.MajorClaimResult.SimilaritiesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='arg_services.mining_explanation.v1beta.MajorClaimResult.SimilaritiesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='arg_services.mining_explanation.v1beta.MajorClaimResult.SimilaritiesEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=620,
  serialized_end=683,
)

_MAJORCLAIMRESULT = _descriptor.Descriptor(
  name='MajorClaimResult',
  full_name='arg_services.mining_explanation.v1beta.MajorClaimResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='similarities', full_name='arg_services.mining_explanation.v1beta.MajorClaimResult.similarities', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='similarities', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keywords', full_name='arg_services.mining_explanation.v1beta.MajorClaimResult.keywords', index=1,
      number=2, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='keywords', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_MAJORCLAIMRESULT_SIMILARITIESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=460,
  serialized_end=683,
)

_MAJORCLAIMREQUEST.fields_by_name['extras'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_MAJORCLAIMRESPONSE.fields_by_name['major_claims'].message_type = _MAJORCLAIMRESULT
_MAJORCLAIMRESPONSE.fields_by_name['extras'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_MAJORCLAIMRESULT_SIMILARITIESENTRY.containing_type = _MAJORCLAIMRESULT
_MAJORCLAIMRESULT.fields_by_name['similarities'].message_type = _MAJORCLAIMRESULT_SIMILARITIESENTRY
DESCRIPTOR.message_types_by_name['MajorClaimRequest'] = _MAJORCLAIMREQUEST
DESCRIPTOR.message_types_by_name['MajorClaimResponse'] = _MAJORCLAIMRESPONSE
DESCRIPTOR.message_types_by_name['MajorClaimResult'] = _MAJORCLAIMRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MajorClaimRequest = _reflection.GeneratedProtocolMessageType('MajorClaimRequest', (_message.Message,), {
  'DESCRIPTOR' : _MAJORCLAIMREQUEST,
  '__module__' : 'arg_services.mining_explanation.v1beta.major_claim_pb2'
  # @@protoc_insertion_point(class_scope:arg_services.mining_explanation.v1beta.MajorClaimRequest)
  })
_sym_db.RegisterMessage(MajorClaimRequest)

MajorClaimResponse = _reflection.GeneratedProtocolMessageType('MajorClaimResponse', (_message.Message,), {
  'DESCRIPTOR' : _MAJORCLAIMRESPONSE,
  '__module__' : 'arg_services.mining_explanation.v1beta.major_claim_pb2'
  # @@protoc_insertion_point(class_scope:arg_services.mining_explanation.v1beta.MajorClaimResponse)
  })
_sym_db.RegisterMessage(MajorClaimResponse)

MajorClaimResult = _reflection.GeneratedProtocolMessageType('MajorClaimResult', (_message.Message,), {

  'SimilaritiesEntry' : _reflection.GeneratedProtocolMessageType('SimilaritiesEntry', (_message.Message,), {
    'DESCRIPTOR' : _MAJORCLAIMRESULT_SIMILARITIESENTRY,
    '__module__' : 'arg_services.mining_explanation.v1beta.major_claim_pb2'
    # @@protoc_insertion_point(class_scope:arg_services.mining_explanation.v1beta.MajorClaimResult.SimilaritiesEntry)
    })
  ,
  'DESCRIPTOR' : _MAJORCLAIMRESULT,
  '__module__' : 'arg_services.mining_explanation.v1beta.major_claim_pb2'
  # @@protoc_insertion_point(class_scope:arg_services.mining_explanation.v1beta.MajorClaimResult)
  })
_sym_db.RegisterMessage(MajorClaimResult)
_sym_db.RegisterMessage(MajorClaimResult.SimilaritiesEntry)


DESCRIPTOR._options = None
_MAJORCLAIMRESULT_SIMILARITIESENTRY._options = None

_MAJORCLAIMEXPLANATIONSERVICE = _descriptor.ServiceDescriptor(
  name='MajorClaimExplanationService',
  full_name='arg_services.mining_explanation.v1beta.MajorClaimExplanationService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=686,
  serialized_end=878,
  methods=[
  _descriptor.MethodDescriptor(
    name='MajorClaim',
    full_name='arg_services.mining_explanation.v1beta.MajorClaimExplanationService.MajorClaim',
    index=0,
    containing_service=None,
    input_type=_MAJORCLAIMREQUEST,
    output_type=_MAJORCLAIMRESPONSE,
    serialized_options=b'\202\323\344\223\002\024:\001*\"\017/nlp/v1/vectors',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MAJORCLAIMEXPLANATIONSERVICE)

DESCRIPTOR.services_by_name['MajorClaimExplanationService'] = _MAJORCLAIMEXPLANATIONSERVICE

# @@protoc_insertion_point(module_scope)
