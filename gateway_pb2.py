# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import celaut_pb2 as celaut__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gateway.proto',
  package='gateway',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rgateway.proto\x12\x07gateway\x1a\x0c\x63\x65laut.proto\"\x07\n\x05\x45mpty\"\x1d\n\x0cTokenMessage\x12\r\n\x05token\x18\x01 \x01(\t\"\x1b\n\x0b\x43ostMessage\x12\x0c\n\x04\x63ost\x18\x01 \x01(\x05\"\x90\x01\n\x08Instance\x12\x30\n\rinstance_meta\x18\x01 \x01(\x0b\x32\x14.celaut.Any.MetadataH\x00\x88\x01\x01\x12\"\n\x08instance\x18\x02 \x01(\x0b\x32\x10.celaut.Instance\x12\x12\n\x05token\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\x10\n\x0e_instance_metaB\x08\n\x06_token\"h\n\x0eHashWithConfig\x12/\n\x04hash\x18\x01 \x01(\x0b\x32!.celaut.Any.Metadata.HashTag.Hash\x12%\n\x06\x63onfig\x18\x03 \x01(\x0b\x32\x15.celaut.Configuration\"X\n\x11ServiceWithConfig\x12\x1c\n\x07service\x18\x02 \x01(\x0b\x32\x0b.celaut.Any\x12%\n\x06\x63onfig\x18\x03 \x01(\x0b\x32\x15.celaut.Configuration\"I\n\x06\x42uffer\x12\x0f\n\x05\x63hunk\x18\x01 \x01(\x0cH\x00\x12\x13\n\tseparator\x18\x02 \x01(\x05H\x00\x12\x10\n\x06signal\x18\x03 \x01(\x0cH\x00\x42\x07\n\x05oneof2\xd0\x02\n\x07Gateway\x12\x36\n\x0cStartService\x12\x0f.gateway.Buffer\x1a\x0f.gateway.Buffer\"\x00(\x01\x30\x01\x12\x35\n\x0bStopService\x12\x0f.gateway.Buffer\x1a\x0f.gateway.Buffer\"\x00(\x01\x30\x01\x12\x30\n\x06Hynode\x12\x0f.gateway.Buffer\x1a\x0f.gateway.Buffer\"\x00(\x01\x30\x01\x12\x31\n\x07GetFile\x12\x0f.gateway.Buffer\x1a\x0f.gateway.Buffer\"\x00(\x01\x30\x01\x12\x37\n\rGetServiceTar\x12\x0f.gateway.Buffer\x1a\x0f.gateway.Buffer\"\x00(\x01\x30\x01\x12\x38\n\x0eGetServiceCost\x12\x0f.gateway.Buffer\x1a\x0f.gateway.Buffer\"\x00(\x01\x30\x01\x62\x06proto3'
  ,
  dependencies=[celaut__pb2.DESCRIPTOR,])




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='gateway.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=40,
  serialized_end=47,
)


_TOKENMESSAGE = _descriptor.Descriptor(
  name='TokenMessage',
  full_name='gateway.TokenMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='gateway.TokenMessage.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=49,
  serialized_end=78,
)


_COSTMESSAGE = _descriptor.Descriptor(
  name='CostMessage',
  full_name='gateway.CostMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cost', full_name='gateway.CostMessage.cost', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=80,
  serialized_end=107,
)


_INSTANCE = _descriptor.Descriptor(
  name='Instance',
  full_name='gateway.Instance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_meta', full_name='gateway.Instance.instance_meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instance', full_name='gateway.Instance.instance', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='gateway.Instance.token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='_instance_meta', full_name='gateway.Instance._instance_meta',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_token', full_name='gateway.Instance._token',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=110,
  serialized_end=254,
)


_HASHWITHCONFIG = _descriptor.Descriptor(
  name='HashWithConfig',
  full_name='gateway.HashWithConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='gateway.HashWithConfig.hash', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='gateway.HashWithConfig.config', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=256,
  serialized_end=360,
)


_SERVICEWITHCONFIG = _descriptor.Descriptor(
  name='ServiceWithConfig',
  full_name='gateway.ServiceWithConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='gateway.ServiceWithConfig.service', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='gateway.ServiceWithConfig.config', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=362,
  serialized_end=450,
)


_BUFFER = _descriptor.Descriptor(
  name='Buffer',
  full_name='gateway.Buffer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chunk', full_name='gateway.Buffer.chunk', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='separator', full_name='gateway.Buffer.separator', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signal', full_name='gateway.Buffer.signal', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='oneof', full_name='gateway.Buffer.oneof',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=452,
  serialized_end=525,
)

_INSTANCE.fields_by_name['instance_meta'].message_type = celaut__pb2._ANY_METADATA
_INSTANCE.fields_by_name['instance'].message_type = celaut__pb2._INSTANCE
_INSTANCE.oneofs_by_name['_instance_meta'].fields.append(
  _INSTANCE.fields_by_name['instance_meta'])
_INSTANCE.fields_by_name['instance_meta'].containing_oneof = _INSTANCE.oneofs_by_name['_instance_meta']
_INSTANCE.oneofs_by_name['_token'].fields.append(
  _INSTANCE.fields_by_name['token'])
_INSTANCE.fields_by_name['token'].containing_oneof = _INSTANCE.oneofs_by_name['_token']
_HASHWITHCONFIG.fields_by_name['hash'].message_type = celaut__pb2._ANY_METADATA_HASHTAG_HASH
_HASHWITHCONFIG.fields_by_name['config'].message_type = celaut__pb2._CONFIGURATION
_SERVICEWITHCONFIG.fields_by_name['service'].message_type = celaut__pb2._ANY
_SERVICEWITHCONFIG.fields_by_name['config'].message_type = celaut__pb2._CONFIGURATION
_BUFFER.oneofs_by_name['oneof'].fields.append(
  _BUFFER.fields_by_name['chunk'])
_BUFFER.fields_by_name['chunk'].containing_oneof = _BUFFER.oneofs_by_name['oneof']
_BUFFER.oneofs_by_name['oneof'].fields.append(
  _BUFFER.fields_by_name['separator'])
_BUFFER.fields_by_name['separator'].containing_oneof = _BUFFER.oneofs_by_name['oneof']
_BUFFER.oneofs_by_name['oneof'].fields.append(
  _BUFFER.fields_by_name['signal'])
_BUFFER.fields_by_name['signal'].containing_oneof = _BUFFER.oneofs_by_name['oneof']
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['TokenMessage'] = _TOKENMESSAGE
DESCRIPTOR.message_types_by_name['CostMessage'] = _COSTMESSAGE
DESCRIPTOR.message_types_by_name['Instance'] = _INSTANCE
DESCRIPTOR.message_types_by_name['HashWithConfig'] = _HASHWITHCONFIG
DESCRIPTOR.message_types_by_name['ServiceWithConfig'] = _SERVICEWITHCONFIG
DESCRIPTOR.message_types_by_name['Buffer'] = _BUFFER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.Empty)
  })
_sym_db.RegisterMessage(Empty)

TokenMessage = _reflection.GeneratedProtocolMessageType('TokenMessage', (_message.Message,), {
  'DESCRIPTOR' : _TOKENMESSAGE,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.TokenMessage)
  })
_sym_db.RegisterMessage(TokenMessage)

CostMessage = _reflection.GeneratedProtocolMessageType('CostMessage', (_message.Message,), {
  'DESCRIPTOR' : _COSTMESSAGE,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.CostMessage)
  })
_sym_db.RegisterMessage(CostMessage)

Instance = _reflection.GeneratedProtocolMessageType('Instance', (_message.Message,), {
  'DESCRIPTOR' : _INSTANCE,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.Instance)
  })
_sym_db.RegisterMessage(Instance)

HashWithConfig = _reflection.GeneratedProtocolMessageType('HashWithConfig', (_message.Message,), {
  'DESCRIPTOR' : _HASHWITHCONFIG,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.HashWithConfig)
  })
_sym_db.RegisterMessage(HashWithConfig)

ServiceWithConfig = _reflection.GeneratedProtocolMessageType('ServiceWithConfig', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEWITHCONFIG,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.ServiceWithConfig)
  })
_sym_db.RegisterMessage(ServiceWithConfig)

Buffer = _reflection.GeneratedProtocolMessageType('Buffer', (_message.Message,), {
  'DESCRIPTOR' : _BUFFER,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.Buffer)
  })
_sym_db.RegisterMessage(Buffer)



_GATEWAY = _descriptor.ServiceDescriptor(
  name='Gateway',
  full_name='gateway.Gateway',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=528,
  serialized_end=864,
  methods=[
  _descriptor.MethodDescriptor(
    name='StartService',
    full_name='gateway.Gateway.StartService',
    index=0,
    containing_service=None,
    input_type=_BUFFER,
    output_type=_BUFFER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StopService',
    full_name='gateway.Gateway.StopService',
    index=1,
    containing_service=None,
    input_type=_BUFFER,
    output_type=_BUFFER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Hynode',
    full_name='gateway.Gateway.Hynode',
    index=2,
    containing_service=None,
    input_type=_BUFFER,
    output_type=_BUFFER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetFile',
    full_name='gateway.Gateway.GetFile',
    index=3,
    containing_service=None,
    input_type=_BUFFER,
    output_type=_BUFFER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetServiceTar',
    full_name='gateway.Gateway.GetServiceTar',
    index=4,
    containing_service=None,
    input_type=_BUFFER,
    output_type=_BUFFER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetServiceCost',
    full_name='gateway.Gateway.GetServiceCost',
    index=5,
    containing_service=None,
    input_type=_BUFFER,
    output_type=_BUFFER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GATEWAY)

DESCRIPTOR.services_by_name['Gateway'] = _GATEWAY

# @@protoc_insertion_point(module_scope)
