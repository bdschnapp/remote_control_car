# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: control.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='control.proto',
  package='control',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rcontrol.proto\x12\x07\x63ontrol\"\x1f\n\x0bturnRequest\x12\x10\n\x08position\x18\x01 \x01(\x05\"\x1c\n\tturnReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x1d\n\x0cspeedRequest\x12\r\n\x05speed\x18\x01 \x01(\x05\"\x1d\n\nspeedReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32t\n\x07\x43ontrol\x12\x32\n\x04turn\x12\x14.control.turnRequest\x1a\x12.control.turnReply\"\x00\x12\x35\n\x05speed\x12\x15.control.speedRequest\x1a\x13.control.speedReply\"\x00\x62\x06proto3'
)




_TURNREQUEST = _descriptor.Descriptor(
  name='turnRequest',
  full_name='control.turnRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='control.turnRequest.position', index=0,
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
  serialized_start=26,
  serialized_end=57,
)


_TURNREPLY = _descriptor.Descriptor(
  name='turnReply',
  full_name='control.turnReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='control.turnReply.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=59,
  serialized_end=87,
)


_SPEEDREQUEST = _descriptor.Descriptor(
  name='speedRequest',
  full_name='control.speedRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='speed', full_name='control.speedRequest.speed', index=0,
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
  serialized_start=89,
  serialized_end=118,
)


_SPEEDREPLY = _descriptor.Descriptor(
  name='speedReply',
  full_name='control.speedReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='control.speedReply.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=120,
  serialized_end=149,
)

DESCRIPTOR.message_types_by_name['turnRequest'] = _TURNREQUEST
DESCRIPTOR.message_types_by_name['turnReply'] = _TURNREPLY
DESCRIPTOR.message_types_by_name['speedRequest'] = _SPEEDREQUEST
DESCRIPTOR.message_types_by_name['speedReply'] = _SPEEDREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

turnRequest = _reflection.GeneratedProtocolMessageType('turnRequest', (_message.Message,), {
  'DESCRIPTOR' : _TURNREQUEST,
  '__module__' : 'control_pb2'
  # @@protoc_insertion_point(class_scope:control.turnRequest)
  })
_sym_db.RegisterMessage(turnRequest)

turnReply = _reflection.GeneratedProtocolMessageType('turnReply', (_message.Message,), {
  'DESCRIPTOR' : _TURNREPLY,
  '__module__' : 'control_pb2'
  # @@protoc_insertion_point(class_scope:control.turnReply)
  })
_sym_db.RegisterMessage(turnReply)

speedRequest = _reflection.GeneratedProtocolMessageType('speedRequest', (_message.Message,), {
  'DESCRIPTOR' : _SPEEDREQUEST,
  '__module__' : 'control_pb2'
  # @@protoc_insertion_point(class_scope:control.speedRequest)
  })
_sym_db.RegisterMessage(speedRequest)

speedReply = _reflection.GeneratedProtocolMessageType('speedReply', (_message.Message,), {
  'DESCRIPTOR' : _SPEEDREPLY,
  '__module__' : 'control_pb2'
  # @@protoc_insertion_point(class_scope:control.speedReply)
  })
_sym_db.RegisterMessage(speedReply)



_CONTROL = _descriptor.ServiceDescriptor(
  name='Control',
  full_name='control.Control',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=151,
  serialized_end=267,
  methods=[
  _descriptor.MethodDescriptor(
    name='turn',
    full_name='control.Control.turn',
    index=0,
    containing_service=None,
    input_type=_TURNREQUEST,
    output_type=_TURNREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='speed',
    full_name='control.Control.speed',
    index=1,
    containing_service=None,
    input_type=_SPEEDREQUEST,
    output_type=_SPEEDREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONTROL)

DESCRIPTOR.services_by_name['Control'] = _CONTROL

# @@protoc_insertion_point(module_scope)
