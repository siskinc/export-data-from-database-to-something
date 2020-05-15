# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='config.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0c\x63onfig.proto\"7\n\x05Model\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x66ields\x18\x02 \x03(\t\x12\x10\n\x08\x63omments\x18\x03 \x03(\t\"\xdf\x01\n\x13\x44\x61taBaseInformation\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\x05\x12\x15\n\rdatabase_name\x18\x05 \x01(\t\x12\x16\n\x0e\x64\x61ta_base_type\x18\x06 \x01(\x05\x12,\n\x04misc\x18\x07 \x03(\x0b\x32\x1e.DataBaseInformation.MiscEntry\x1a+\n\tMiscEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x9b\x01\n\x11\x45xportInformation\x12\x18\n\x10output_file_path\x18\x01 \x01(\t\x12*\n\x04misc\x18\x02 \x03(\x0b\x32\x1c.ExportInformation.MiscEntry\x12\x13\n\x0b\x65xport_type\x18\x03 \x01(\x05\x1a+\n\tMiscEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x9c\x01\n\x0eJobInformation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05where\x18\x02 \x01(\t\x12\x12\n\nbatch_size\x18\x03 \x01(\r\x12&\n\x08\x64\x61tabase\x18\x04 \x01(\x0b\x32\x14.DataBaseInformation\x12\"\n\x06\x65xport\x18\x05 \x01(\x0b\x32\x12.ExportInformation\x12\r\n\x05model\x18\x06 \x01(\t\"j\n\tConfigure\x12&\n\x08\x64\x61tabase\x18\x01 \x01(\x0b\x32\x14.DataBaseInformation\x12\x16\n\x06models\x18\x02 \x03(\x0b\x32\x06.Model\x12\x1d\n\x04jobs\x18\x03 \x03(\x0b\x32\x0f.JobInformation*=\n\x0c\x44\x61taBaseType\x12\x15\n\x11\x44\x61taBaseTypeMysql\x10\x00\x12\x16\n\x12\x44\x61taBaseTypeInflux\x10\x01*4\n\nExportType\x12\x13\n\x0f\x45xportTypeExcel\x10\x00\x12\x11\n\rExportTypeCsv\x10\x01\x62\x06proto3'
)

_DATABASETYPE = _descriptor.EnumDescriptor(
  name='DataBaseType',
  full_name='DataBaseType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DataBaseTypeMysql', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataBaseTypeInflux', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=724,
  serialized_end=785,
)
_sym_db.RegisterEnumDescriptor(_DATABASETYPE)

DataBaseType = enum_type_wrapper.EnumTypeWrapper(_DATABASETYPE)
_EXPORTTYPE = _descriptor.EnumDescriptor(
  name='ExportType',
  full_name='ExportType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ExportTypeExcel', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ExportTypeCsv', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=787,
  serialized_end=839,
)
_sym_db.RegisterEnumDescriptor(_EXPORTTYPE)

ExportType = enum_type_wrapper.EnumTypeWrapper(_EXPORTTYPE)
DataBaseTypeMysql = 0
DataBaseTypeInflux = 1
ExportTypeExcel = 0
ExportTypeCsv = 1



_MODEL = _descriptor.Descriptor(
  name='Model',
  full_name='Model',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Model.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='Model.fields', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comments', full_name='Model.comments', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=16,
  serialized_end=71,
)


_DATABASEINFORMATION_MISCENTRY = _descriptor.Descriptor(
  name='MiscEntry',
  full_name='DataBaseInformation.MiscEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='DataBaseInformation.MiscEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='DataBaseInformation.MiscEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=254,
  serialized_end=297,
)

_DATABASEINFORMATION = _descriptor.Descriptor(
  name='DataBaseInformation',
  full_name='DataBaseInformation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='DataBaseInformation.host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='DataBaseInformation.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='DataBaseInformation.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='DataBaseInformation.port', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='database_name', full_name='DataBaseInformation.database_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_base_type', full_name='DataBaseInformation.data_base_type', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='misc', full_name='DataBaseInformation.misc', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DATABASEINFORMATION_MISCENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=297,
)


_EXPORTINFORMATION_MISCENTRY = _descriptor.Descriptor(
  name='MiscEntry',
  full_name='ExportInformation.MiscEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ExportInformation.MiscEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ExportInformation.MiscEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=254,
  serialized_end=297,
)

_EXPORTINFORMATION = _descriptor.Descriptor(
  name='ExportInformation',
  full_name='ExportInformation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='output_file_path', full_name='ExportInformation.output_file_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='misc', full_name='ExportInformation.misc', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='export_type', full_name='ExportInformation.export_type', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EXPORTINFORMATION_MISCENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=300,
  serialized_end=455,
)


_JOBINFORMATION = _descriptor.Descriptor(
  name='JobInformation',
  full_name='JobInformation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='JobInformation.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='where', full_name='JobInformation.where', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='JobInformation.batch_size', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='database', full_name='JobInformation.database', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='export', full_name='JobInformation.export', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model', full_name='JobInformation.model', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=458,
  serialized_end=614,
)


_CONFIGURE = _descriptor.Descriptor(
  name='Configure',
  full_name='Configure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='database', full_name='Configure.database', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='models', full_name='Configure.models', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='jobs', full_name='Configure.jobs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=616,
  serialized_end=722,
)

_DATABASEINFORMATION_MISCENTRY.containing_type = _DATABASEINFORMATION
_DATABASEINFORMATION.fields_by_name['misc'].message_type = _DATABASEINFORMATION_MISCENTRY
_EXPORTINFORMATION_MISCENTRY.containing_type = _EXPORTINFORMATION
_EXPORTINFORMATION.fields_by_name['misc'].message_type = _EXPORTINFORMATION_MISCENTRY
_JOBINFORMATION.fields_by_name['database'].message_type = _DATABASEINFORMATION
_JOBINFORMATION.fields_by_name['export'].message_type = _EXPORTINFORMATION
_CONFIGURE.fields_by_name['database'].message_type = _DATABASEINFORMATION
_CONFIGURE.fields_by_name['models'].message_type = _MODEL
_CONFIGURE.fields_by_name['jobs'].message_type = _JOBINFORMATION
DESCRIPTOR.message_types_by_name['Model'] = _MODEL
DESCRIPTOR.message_types_by_name['DataBaseInformation'] = _DATABASEINFORMATION
DESCRIPTOR.message_types_by_name['ExportInformation'] = _EXPORTINFORMATION
DESCRIPTOR.message_types_by_name['JobInformation'] = _JOBINFORMATION
DESCRIPTOR.message_types_by_name['Configure'] = _CONFIGURE
DESCRIPTOR.enum_types_by_name['DataBaseType'] = _DATABASETYPE
DESCRIPTOR.enum_types_by_name['ExportType'] = _EXPORTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Model = _reflection.GeneratedProtocolMessageType('Model', (_message.Message,), {
  'DESCRIPTOR' : _MODEL,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:Model)
  })
_sym_db.RegisterMessage(Model)

DataBaseInformation = _reflection.GeneratedProtocolMessageType('DataBaseInformation', (_message.Message,), {

  'MiscEntry' : _reflection.GeneratedProtocolMessageType('MiscEntry', (_message.Message,), {
    'DESCRIPTOR' : _DATABASEINFORMATION_MISCENTRY,
    '__module__' : 'config_pb2'
    # @@protoc_insertion_point(class_scope:DataBaseInformation.MiscEntry)
    })
  ,
  'DESCRIPTOR' : _DATABASEINFORMATION,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:DataBaseInformation)
  })
_sym_db.RegisterMessage(DataBaseInformation)
_sym_db.RegisterMessage(DataBaseInformation.MiscEntry)

ExportInformation = _reflection.GeneratedProtocolMessageType('ExportInformation', (_message.Message,), {

  'MiscEntry' : _reflection.GeneratedProtocolMessageType('MiscEntry', (_message.Message,), {
    'DESCRIPTOR' : _EXPORTINFORMATION_MISCENTRY,
    '__module__' : 'config_pb2'
    # @@protoc_insertion_point(class_scope:ExportInformation.MiscEntry)
    })
  ,
  'DESCRIPTOR' : _EXPORTINFORMATION,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:ExportInformation)
  })
_sym_db.RegisterMessage(ExportInformation)
_sym_db.RegisterMessage(ExportInformation.MiscEntry)

JobInformation = _reflection.GeneratedProtocolMessageType('JobInformation', (_message.Message,), {
  'DESCRIPTOR' : _JOBINFORMATION,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:JobInformation)
  })
_sym_db.RegisterMessage(JobInformation)

Configure = _reflection.GeneratedProtocolMessageType('Configure', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGURE,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:Configure)
  })
_sym_db.RegisterMessage(Configure)


_DATABASEINFORMATION_MISCENTRY._options = None
_EXPORTINFORMATION_MISCENTRY._options = None
# @@protoc_insertion_point(module_scope)
