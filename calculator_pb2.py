# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calculator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x63\x61lculator.proto\")\n\x11\x43\x61lculatorRequest\x12\t\n\x01\x61\x18\x01 \x02(\x01\x12\t\n\x01\x62\x18\x02 \x02(\x01\"\x1f\n\x0f\x43\x61lculatorReply\x12\x0c\n\x04resp\x18\x03 \x02(\x01\x32\xd2\x01\n\x07Greeter\x12-\n\x03\x61\x64\x64\x12\x12.CalculatorRequest\x1a\x10.CalculatorReply\"\x00\x12\x32\n\x08multiply\x12\x12.CalculatorRequest\x1a\x10.CalculatorReply\"\x00\x12\x30\n\x06\x64ivide\x12\x12.CalculatorRequest\x1a\x10.CalculatorReply\"\x00\x12\x32\n\x08subtract\x12\x12.CalculatorRequest\x1a\x10.CalculatorReply\"\x00')



_CALCULATORREQUEST = DESCRIPTOR.message_types_by_name['CalculatorRequest']
_CALCULATORREPLY = DESCRIPTOR.message_types_by_name['CalculatorReply']
CalculatorRequest = _reflection.GeneratedProtocolMessageType('CalculatorRequest', (_message.Message,), {
  'DESCRIPTOR' : _CALCULATORREQUEST,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:CalculatorRequest)
  })
_sym_db.RegisterMessage(CalculatorRequest)

CalculatorReply = _reflection.GeneratedProtocolMessageType('CalculatorReply', (_message.Message,), {
  'DESCRIPTOR' : _CALCULATORREPLY,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:CalculatorReply)
  })
_sym_db.RegisterMessage(CalculatorReply)

_GREETER = DESCRIPTOR.services_by_name['Greeter']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CALCULATORREQUEST._serialized_start=20
  _CALCULATORREQUEST._serialized_end=61
  _CALCULATORREPLY._serialized_start=63
  _CALCULATORREPLY._serialized_end=94
  _GREETER._serialized_start=97
  _GREETER._serialized_end=307
# @@protoc_insertion_point(module_scope)
