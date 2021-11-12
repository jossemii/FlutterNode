# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: buffer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='buffer.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x62uffer.proto\"\xe0\x02\n\x06\x42uffer\x12\x12\n\x05\x63hunk\x18\x01 \x01(\x0cH\x00\x88\x01\x01\x12\x16\n\tseparator\x18\x02 \x01(\x08H\x01\x88\x01\x01\x12\x13\n\x06signal\x18\x03 \x01(\x08H\x02\x88\x01\x01\x12\x1f\n\x04head\x18\x04 \x01(\x0b\x32\x0c.Buffer.HeadH\x03\x88\x01\x01\x1a\xc7\x01\n\x04Head\x12\r\n\x05index\x18\x01 \x01(\x05\x12*\n\npartitions\x18\x02 \x03(\x0b\x32\x16.Buffer.Head.Partition\x1a\x83\x01\n\tPartition\x12\x30\n\x05index\x18\x01 \x03(\x0b\x32!.Buffer.Head.Partition.IndexEntry\x1a\x44\n\nIndexEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.Buffer.Head.Partition:\x02\x38\x01\x42\x08\n\x06_chunkB\x0c\n\n_separatorB\t\n\x07_signalB\x07\n\x05_headb\x06proto3'
)




_BUFFER_HEAD_PARTITION_INDEXENTRY = _descriptor.Descriptor(
  name='IndexEntry',
  full_name='Buffer.Head.Partition.IndexEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Buffer.Head.Partition.IndexEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='Buffer.Head.Partition.IndexEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=257,
  serialized_end=325,
)

_BUFFER_HEAD_PARTITION = _descriptor.Descriptor(
  name='Partition',
  full_name='Buffer.Head.Partition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='Buffer.Head.Partition.index', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_BUFFER_HEAD_PARTITION_INDEXENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=194,
  serialized_end=325,
)

_BUFFER_HEAD = _descriptor.Descriptor(
  name='Head',
  full_name='Buffer.Head',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='Buffer.Head.index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='partitions', full_name='Buffer.Head.partitions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_BUFFER_HEAD_PARTITION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=325,
)

_BUFFER = _descriptor.Descriptor(
  name='Buffer',
  full_name='Buffer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chunk', full_name='Buffer.chunk', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='separator', full_name='Buffer.separator', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signal', full_name='Buffer.signal', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='head', full_name='Buffer.head', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_BUFFER_HEAD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_chunk', full_name='Buffer._chunk',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_separator', full_name='Buffer._separator',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_signal', full_name='Buffer._signal',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_head', full_name='Buffer._head',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=17,
  serialized_end=369,
)

_BUFFER_HEAD_PARTITION_INDEXENTRY.fields_by_name['value'].message_type = _BUFFER_HEAD_PARTITION
_BUFFER_HEAD_PARTITION_INDEXENTRY.containing_type = _BUFFER_HEAD_PARTITION
_BUFFER_HEAD_PARTITION.fields_by_name['index'].message_type = _BUFFER_HEAD_PARTITION_INDEXENTRY
_BUFFER_HEAD_PARTITION.containing_type = _BUFFER_HEAD
_BUFFER_HEAD.fields_by_name['partitions'].message_type = _BUFFER_HEAD_PARTITION
_BUFFER_HEAD.containing_type = _BUFFER
_BUFFER.fields_by_name['head'].message_type = _BUFFER_HEAD
_BUFFER.oneofs_by_name['_chunk'].fields.append(
  _BUFFER.fields_by_name['chunk'])
_BUFFER.fields_by_name['chunk'].containing_oneof = _BUFFER.oneofs_by_name['_chunk']
_BUFFER.oneofs_by_name['_separator'].fields.append(
  _BUFFER.fields_by_name['separator'])
_BUFFER.fields_by_name['separator'].containing_oneof = _BUFFER.oneofs_by_name['_separator']
_BUFFER.oneofs_by_name['_signal'].fields.append(
  _BUFFER.fields_by_name['signal'])
_BUFFER.fields_by_name['signal'].containing_oneof = _BUFFER.oneofs_by_name['_signal']
_BUFFER.oneofs_by_name['_head'].fields.append(
  _BUFFER.fields_by_name['head'])
_BUFFER.fields_by_name['head'].containing_oneof = _BUFFER.oneofs_by_name['_head']
DESCRIPTOR.message_types_by_name['Buffer'] = _BUFFER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Buffer = _reflection.GeneratedProtocolMessageType('Buffer', (_message.Message,), {

  'Head' : _reflection.GeneratedProtocolMessageType('Head', (_message.Message,), {

    'Partition' : _reflection.GeneratedProtocolMessageType('Partition', (_message.Message,), {

      'IndexEntry' : _reflection.GeneratedProtocolMessageType('IndexEntry', (_message.Message,), {
        'DESCRIPTOR' : _BUFFER_HEAD_PARTITION_INDEXENTRY,
        '__module__' : 'buffer_pb2'
        # @@protoc_insertion_point(class_scope:Buffer.Head.Partition.IndexEntry)
        })
      ,
      'DESCRIPTOR' : _BUFFER_HEAD_PARTITION,
      '__module__' : 'buffer_pb2'
      # @@protoc_insertion_point(class_scope:Buffer.Head.Partition)
      })
    ,
    'DESCRIPTOR' : _BUFFER_HEAD,
    '__module__' : 'buffer_pb2'
    # @@protoc_insertion_point(class_scope:Buffer.Head)
    })
  ,
  'DESCRIPTOR' : _BUFFER,
  '__module__' : 'buffer_pb2'
  # @@protoc_insertion_point(class_scope:Buffer)
  })
_sym_db.RegisterMessage(Buffer)
_sym_db.RegisterMessage(Buffer.Head)
_sym_db.RegisterMessage(Buffer.Head.Partition)
_sym_db.RegisterMessage(Buffer.Head.Partition.IndexEntry)


_BUFFER_HEAD_PARTITION_INDEXENTRY._options = None
# @@protoc_insertion_point(module_scope)
