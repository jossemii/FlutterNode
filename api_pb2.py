# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import onnx_pb2 as onnx__pb2
import ipss_pb2 as ipss__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='api.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tapi.proto\x1a\nonnx.proto\x1a\nipss.proto\"\"\n\x0eInterpretation\x12\x10\n\x08variable\x18\x01 \x03(\x05\"\x19\n\x06\x43lause\x12\x0f\n\x07literal\x18\x01 \x03(\x05\"\x1e\n\x03\x43nf\x12\x17\n\x06\x63lause\x18\x01 \x03(\x0b\x32\x07.Clause\"\x07\n\x05\x45mpty\"\x14\n\x04\x46ile\x12\x0c\n\x04\x66ile\x18\x01 \x01(\t2%\n\x06Random\x12\x1b\n\tRandomCnf\x12\x06.Empty\x1a\x04.Cnf\"\x00\x32\xdf\x01\n\x06Solver\x12\x1e\n\nStartTrain\x12\x06.Empty\x1a\x06.Empty\"\x00\x12\x1d\n\tStopTrain\x12\x06.Empty\x1a\x06.Empty\"\x00\x12*\n\tGetTensor\x12\x06.Empty\x1a\x11.tensor_onnx.ONNX\"\x00\x30\x01\x12\'\n\x0cUploadSolver\x12\r.ipss.Service\x1a\x06.Empty\"\x00\x12\x1f\n\nStreamLogs\x12\x06.Empty\x1a\x05.File\"\x00\x30\x01\x12 \n\x05Solve\x12\x04.Cnf\x1a\x0f.Interpretation\"\x00\x62\x06proto3'
  ,
  dependencies=[onnx__pb2.DESCRIPTOR,ipss__pb2.DESCRIPTOR,])




_INTERPRETATION = _descriptor.Descriptor(
  name='Interpretation',
  full_name='Interpretation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='variable', full_name='Interpretation.variable', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=37,
  serialized_end=71,
)


_CLAUSE = _descriptor.Descriptor(
  name='Clause',
  full_name='Clause',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='literal', full_name='Clause.literal', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=73,
  serialized_end=98,
)


_CNF = _descriptor.Descriptor(
  name='Cnf',
  full_name='Cnf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='clause', full_name='Cnf.clause', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=100,
  serialized_end=130,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
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
  serialized_start=132,
  serialized_end=139,
)


_FILE = _descriptor.Descriptor(
  name='File',
  full_name='File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file', full_name='File.file', index=0,
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
  serialized_start=141,
  serialized_end=161,
)

_CNF.fields_by_name['clause'].message_type = _CLAUSE
DESCRIPTOR.message_types_by_name['Interpretation'] = _INTERPRETATION
DESCRIPTOR.message_types_by_name['Clause'] = _CLAUSE
DESCRIPTOR.message_types_by_name['Cnf'] = _CNF
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['File'] = _FILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Interpretation = _reflection.GeneratedProtocolMessageType('Interpretation', (_message.Message,), {
  'DESCRIPTOR' : _INTERPRETATION,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:Interpretation)
  })
_sym_db.RegisterMessage(Interpretation)

Clause = _reflection.GeneratedProtocolMessageType('Clause', (_message.Message,), {
  'DESCRIPTOR' : _CLAUSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:Clause)
  })
_sym_db.RegisterMessage(Clause)

Cnf = _reflection.GeneratedProtocolMessageType('Cnf', (_message.Message,), {
  'DESCRIPTOR' : _CNF,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:Cnf)
  })
_sym_db.RegisterMessage(Cnf)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), {
  'DESCRIPTOR' : _FILE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:File)
  })
_sym_db.RegisterMessage(File)



_RANDOM = _descriptor.ServiceDescriptor(
  name='Random',
  full_name='Random',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=163,
  serialized_end=200,
  methods=[
  _descriptor.MethodDescriptor(
    name='RandomCnf',
    full_name='Random.RandomCnf',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_CNF,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RANDOM)

DESCRIPTOR.services_by_name['Random'] = _RANDOM


_SOLVER = _descriptor.ServiceDescriptor(
  name='Solver',
  full_name='Solver',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=203,
  serialized_end=426,
  methods=[
  _descriptor.MethodDescriptor(
    name='StartTrain',
    full_name='Solver.StartTrain',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StopTrain',
    full_name='Solver.StopTrain',
    index=1,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetTensor',
    full_name='Solver.GetTensor',
    index=2,
    containing_service=None,
    input_type=_EMPTY,
    output_type=onnx__pb2._ONNX,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UploadSolver',
    full_name='Solver.UploadSolver',
    index=3,
    containing_service=None,
    input_type=ipss__pb2._SERVICE,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamLogs',
    full_name='Solver.StreamLogs',
    index=4,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_FILE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Solve',
    full_name='Solver.Solve',
    index=5,
    containing_service=None,
    input_type=_CNF,
    output_type=_INTERPRETATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SOLVER)

DESCRIPTOR.services_by_name['Solver'] = _SOLVER

# @@protoc_insertion_point(module_scope)
