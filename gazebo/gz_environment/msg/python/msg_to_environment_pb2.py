# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msg_to_environment.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='msg_to_environment.proto',
  package='',
  serialized_pb=_b('\n\x18msg_to_environment.proto\"`\n\x10MsgToEnvironment\x12\x17\n\x0flinear_velocity\x18\x01 \x02(\x02\x12\x18\n\x10\x61ngular_velocity\x18\x02 \x02(\x02\x12\x19\n\x11reset_environment\x18\x03 \x02(\x08')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MSGTOENVIRONMENT = _descriptor.Descriptor(
  name='MsgToEnvironment',
  full_name='MsgToEnvironment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='linear_velocity', full_name='MsgToEnvironment.linear_velocity', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='angular_velocity', full_name='MsgToEnvironment.angular_velocity', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reset_environment', full_name='MsgToEnvironment.reset_environment', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=124,
)

DESCRIPTOR.message_types_by_name['MsgToEnvironment'] = _MSGTOENVIRONMENT

MsgToEnvironment = _reflection.GeneratedProtocolMessageType('MsgToEnvironment', (_message.Message,), dict(
  DESCRIPTOR = _MSGTOENVIRONMENT,
  __module__ = 'msg_to_environment_pb2'
  # @@protoc_insertion_point(class_scope:MsgToEnvironment)
  ))
_sym_db.RegisterMessage(MsgToEnvironment)


# @@protoc_insertion_point(module_scope)
