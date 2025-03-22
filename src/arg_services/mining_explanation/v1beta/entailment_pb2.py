# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arg_services/mining_explanation/v1beta/entailment.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from arg_services.mining.v1beta import entailment_pb2 as arg__services_dot_mining_dot_v1beta_dot_entailment__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='arg_services/mining_explanation/v1beta/entailment.proto',
  package='arg_services.mining_explanation.v1beta',
  syntax='proto3',
  serialized_options=b'\n*com.arg_services.mining_explanation.v1betaB\017EntailmentProtoP\001\242\002\003AMX\252\002$ArgServices.MiningExplanation.V1beta\312\002$ArgServices\\MiningExplanation\\V1beta\342\0020ArgServices\\MiningExplanation\\V1beta\\GPBMetadata\352\002&ArgServices::MiningExplanation::V1beta',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n7arg_services/mining_explanation/v1beta/entailment.proto\x12&arg_services.mining_explanation.v1beta\x1a+arg_services/mining/v1beta/entailment.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xb7\x01\n\x12\x45ntailmentsRequest\x12\x1a\n\x08language\x18\x01 \x01(\tR\x08language\x12T\n\x0b\x65ntailments\x18\x02 \x03(\x0b\x32\x32.arg_services.mining_explanation.v1beta.EntailmentR\x0b\x65ntailments\x12/\n\x06\x65xtras\x18\x0f \x01(\x0b\x32\x17.google.protobuf.StructR\x06\x65xtras\"\x9a\x01\n\x13\x45ntailmentsResponse\x12R\n\x07results\x18\x01 \x03(\x0b\x32\x38.arg_services.mining_explanation.v1beta.EntailmentResultR\x07results\x12/\n\x06\x65xtras\x18\x0f \x01(\x0b\x32\x17.google.protobuf.StructR\x06\x65xtras\"|\n\nEntailment\x12\x18\n\x07premise\x18\x01 \x01(\tR\x07premise\x12\x14\n\x05\x63laim\x18\x02 \x01(\tR\x05\x63laim\x12>\n\x04type\x18\x03 \x01(\x0e\x32*.arg_services.mining.v1beta.EntailmentTypeR\x04type\"\x95\x02\n\x10\x45ntailmentResult\x12n\n\x0csimilarities\x18\x01 \x03(\x0b\x32J.arg_services.mining_explanation.v1beta.EntailmentResult.SimilaritiesEntryR\x0csimilarities\x12)\n\x10keywords_premise\x18\x02 \x03(\x08R\x0fkeywordsPremise\x12%\n\x0ekeywords_claim\x18\x03 \x03(\x08R\rkeywordsClaim\x1a?\n\x11SimilaritiesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x01R\x05value:\x02\x38\x01\x32\xda\x01\n\x1c\x45ntailmentExplanationService\x12\xb9\x01\n\x0b\x45ntailments\x12:.arg_services.mining_explanation.v1beta.EntailmentsRequest\x1a;.arg_services.mining_explanation.v1beta.EntailmentsResponse\"1\x82\xd3\xe4\x93\x02+:\x01*\"&/mining_explanation/v1beta/entailmentsB\xef\x01\n*com.arg_services.mining_explanation.v1betaB\x0f\x45ntailmentProtoP\x01\xa2\x02\x03\x41MX\xaa\x02$ArgServices.MiningExplanation.V1beta\xca\x02$ArgServices\\MiningExplanation\\V1beta\xe2\x02\x30\x41rgServices\\MiningExplanation\\V1beta\\GPBMetadata\xea\x02&ArgServices::MiningExplanation::V1betab\x06proto3'
  ,
  dependencies=[arg__services_dot_mining_dot_v1beta_dot_entailment__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_ENTAILMENTSREQUEST = _descriptor.Descriptor(
  name='EntailmentsRequest',
  full_name='arg_services.mining_explanation.v1beta.EntailmentsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='language', full_name='arg_services.mining_explanation.v1beta.EntailmentsRequest.language', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='language', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entailments', full_name='arg_services.mining_explanation.v1beta.EntailmentsRequest.entailments', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='entailments', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extras', full_name='arg_services.mining_explanation.v1beta.EntailmentsRequest.extras', index=2,
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
  serialized_start=205,
  serialized_end=388,
)


_ENTAILMENTSRESPONSE = _descriptor.Descriptor(
  name='EntailmentsResponse',
  full_name='arg_services.mining_explanation.v1beta.EntailmentsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='arg_services.mining_explanation.v1beta.EntailmentsResponse.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='results', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extras', full_name='arg_services.mining_explanation.v1beta.EntailmentsResponse.extras', index=1,
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
  serialized_start=391,
  serialized_end=545,
)


_ENTAILMENT = _descriptor.Descriptor(
  name='Entailment',
  full_name='arg_services.mining_explanation.v1beta.Entailment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='premise', full_name='arg_services.mining_explanation.v1beta.Entailment.premise', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='premise', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='claim', full_name='arg_services.mining_explanation.v1beta.Entailment.claim', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='claim', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='arg_services.mining_explanation.v1beta.Entailment.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='type', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=547,
  serialized_end=671,
)


_ENTAILMENTRESULT_SIMILARITIESENTRY = _descriptor.Descriptor(
  name='SimilaritiesEntry',
  full_name='arg_services.mining_explanation.v1beta.EntailmentResult.SimilaritiesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='arg_services.mining_explanation.v1beta.EntailmentResult.SimilaritiesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='arg_services.mining_explanation.v1beta.EntailmentResult.SimilaritiesEntry.value', index=1,
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
  serialized_start=888,
  serialized_end=951,
)

_ENTAILMENTRESULT = _descriptor.Descriptor(
  name='EntailmentResult',
  full_name='arg_services.mining_explanation.v1beta.EntailmentResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='similarities', full_name='arg_services.mining_explanation.v1beta.EntailmentResult.similarities', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='similarities', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keywords_premise', full_name='arg_services.mining_explanation.v1beta.EntailmentResult.keywords_premise', index=1,
      number=2, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='keywordsPremise', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keywords_claim', full_name='arg_services.mining_explanation.v1beta.EntailmentResult.keywords_claim', index=2,
      number=3, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='keywordsClaim', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ENTAILMENTRESULT_SIMILARITIESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=674,
  serialized_end=951,
)

_ENTAILMENTSREQUEST.fields_by_name['entailments'].message_type = _ENTAILMENT
_ENTAILMENTSREQUEST.fields_by_name['extras'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_ENTAILMENTSRESPONSE.fields_by_name['results'].message_type = _ENTAILMENTRESULT
_ENTAILMENTSRESPONSE.fields_by_name['extras'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_ENTAILMENT.fields_by_name['type'].enum_type = arg__services_dot_mining_dot_v1beta_dot_entailment__pb2._ENTAILMENTTYPE
_ENTAILMENTRESULT_SIMILARITIESENTRY.containing_type = _ENTAILMENTRESULT
_ENTAILMENTRESULT.fields_by_name['similarities'].message_type = _ENTAILMENTRESULT_SIMILARITIESENTRY
DESCRIPTOR.message_types_by_name['EntailmentsRequest'] = _ENTAILMENTSREQUEST
DESCRIPTOR.message_types_by_name['EntailmentsResponse'] = _ENTAILMENTSRESPONSE
DESCRIPTOR.message_types_by_name['Entailment'] = _ENTAILMENT
DESCRIPTOR.message_types_by_name['EntailmentResult'] = _ENTAILMENTRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EntailmentsRequest = _reflection.GeneratedProtocolMessageType('EntailmentsRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENTAILMENTSREQUEST,
  '__module__' : 'arg_services.mining_explanation.v1beta.entailment_pb2'
  # @@protoc_insertion_point(class_scope:arg_services.mining_explanation.v1beta.EntailmentsRequest)
  })
_sym_db.RegisterMessage(EntailmentsRequest)

EntailmentsResponse = _reflection.GeneratedProtocolMessageType('EntailmentsResponse', (_message.Message,), {
  'DESCRIPTOR' : _ENTAILMENTSRESPONSE,
  '__module__' : 'arg_services.mining_explanation.v1beta.entailment_pb2'
  # @@protoc_insertion_point(class_scope:arg_services.mining_explanation.v1beta.EntailmentsResponse)
  })
_sym_db.RegisterMessage(EntailmentsResponse)

Entailment = _reflection.GeneratedProtocolMessageType('Entailment', (_message.Message,), {
  'DESCRIPTOR' : _ENTAILMENT,
  '__module__' : 'arg_services.mining_explanation.v1beta.entailment_pb2'
  # @@protoc_insertion_point(class_scope:arg_services.mining_explanation.v1beta.Entailment)
  })
_sym_db.RegisterMessage(Entailment)

EntailmentResult = _reflection.GeneratedProtocolMessageType('EntailmentResult', (_message.Message,), {

  'SimilaritiesEntry' : _reflection.GeneratedProtocolMessageType('SimilaritiesEntry', (_message.Message,), {
    'DESCRIPTOR' : _ENTAILMENTRESULT_SIMILARITIESENTRY,
    '__module__' : 'arg_services.mining_explanation.v1beta.entailment_pb2'
    # @@protoc_insertion_point(class_scope:arg_services.mining_explanation.v1beta.EntailmentResult.SimilaritiesEntry)
    })
  ,
  'DESCRIPTOR' : _ENTAILMENTRESULT,
  '__module__' : 'arg_services.mining_explanation.v1beta.entailment_pb2'
  # @@protoc_insertion_point(class_scope:arg_services.mining_explanation.v1beta.EntailmentResult)
  })
_sym_db.RegisterMessage(EntailmentResult)
_sym_db.RegisterMessage(EntailmentResult.SimilaritiesEntry)


DESCRIPTOR._options = None
_ENTAILMENTRESULT_SIMILARITIESENTRY._options = None

_ENTAILMENTEXPLANATIONSERVICE = _descriptor.ServiceDescriptor(
  name='EntailmentExplanationService',
  full_name='arg_services.mining_explanation.v1beta.EntailmentExplanationService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=954,
  serialized_end=1172,
  methods=[
  _descriptor.MethodDescriptor(
    name='Entailments',
    full_name='arg_services.mining_explanation.v1beta.EntailmentExplanationService.Entailments',
    index=0,
    containing_service=None,
    input_type=_ENTAILMENTSREQUEST,
    output_type=_ENTAILMENTSRESPONSE,
    serialized_options=b'\202\323\344\223\002+:\001*\"&/mining_explanation/v1beta/entailments',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ENTAILMENTEXPLANATIONSERVICE)

DESCRIPTOR.services_by_name['EntailmentExplanationService'] = _ENTAILMENTEXPLANATIONSERVICE

# @@protoc_insertion_point(module_scope)
