# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: learner.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='learner.proto',
  package='academy',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\rlearner.proto\x12\x07\x61\x63\x61\x64\x65my\"m\n\x07Learner\x12\'\n\x04task\x18\x01 \x01(\x0e\x32\x19.academy.Learner.TaskType\x12\x0e\n\x06\x61\x63tion\x18\x04 \x01(\x02\")\n\x08TaskType\x12\t\n\x05START\x10\x00\x12\t\n\x05RESET\x10\x01\x12\x07\n\x03\x45ND\x10\x02')
)



_LEARNER_TASKTYPE = _descriptor.EnumDescriptor(
  name='TaskType',
  full_name='academy.Learner.TaskType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='START', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESET', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=94,
  serialized_end=135,
)
_sym_db.RegisterEnumDescriptor(_LEARNER_TASKTYPE)


_LEARNER = _descriptor.Descriptor(
  name='Learner',
  full_name='academy.Learner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task', full_name='academy.Learner.task', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='academy.Learner.action', index=1,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LEARNER_TASKTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=135,
)

_LEARNER.fields_by_name['task'].enum_type = _LEARNER_TASKTYPE
_LEARNER_TASKTYPE.containing_type = _LEARNER
DESCRIPTOR.message_types_by_name['Learner'] = _LEARNER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Learner = _reflection.GeneratedProtocolMessageType('Learner', (_message.Message,), {
  'DESCRIPTOR' : _LEARNER,
  '__module__' : 'learner_pb2'
  # @@protoc_insertion_point(class_scope:academy.Learner)
  })
_sym_db.RegisterMessage(Learner)


# @@protoc_insertion_point(module_scope)
