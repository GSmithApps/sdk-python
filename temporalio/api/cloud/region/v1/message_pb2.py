# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal/api/cloud/region/v1/message.proto
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n*temporal/api/cloud/region/v1/message.proto\x12\x1ctemporal.api.cloud.region.v1"\x99\x02\n\x06Region\x12\n\n\x02id\x18\x01 \x01(\t\x12%\n\x19\x63loud_provider_deprecated\x18\x02 \x01(\tB\x02\x18\x01\x12J\n\x0e\x63loud_provider\x18\x05 \x01(\x0e\x32\x32.temporal.api.cloud.region.v1.Region.CloudProvider\x12\x1d\n\x15\x63loud_provider_region\x18\x03 \x01(\t\x12\x10\n\x08location\x18\x04 \x01(\t"_\n\rCloudProvider\x12\x1e\n\x1a\x43LOUD_PROVIDER_UNSPECIFIED\x10\x00\x12\x16\n\x12\x43LOUD_PROVIDER_AWS\x10\x01\x12\x16\n\x12\x43LOUD_PROVIDER_GCP\x10\x02\x42\xa2\x01\n\x1fio.temporal.api.cloud.region.v1B\x0cMessageProtoP\x01Z)go.temporal.io/api/cloud/region/v1;region\xaa\x02\x1eTemporalio.Api.Cloud.Region.V1\xea\x02"Temporalio::Api::Cloud::Region::V1b\x06proto3'
)


_REGION = DESCRIPTOR.message_types_by_name["Region"]
_REGION_CLOUDPROVIDER = _REGION.enum_types_by_name["CloudProvider"]
Region = _reflection.GeneratedProtocolMessageType(
    "Region",
    (_message.Message,),
    {
        "DESCRIPTOR": _REGION,
        "__module__": "temporal.api.cloud.region.v1.message_pb2",
        # @@protoc_insertion_point(class_scope:temporal.api.cloud.region.v1.Region)
    },
)
_sym_db.RegisterMessage(Region)

if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\037io.temporal.api.cloud.region.v1B\014MessageProtoP\001Z)go.temporal.io/api/cloud/region/v1;region\252\002\036Temporalio.Api.Cloud.Region.V1\352\002"Temporalio::Api::Cloud::Region::V1'
    _REGION.fields_by_name["cloud_provider_deprecated"]._options = None
    _REGION.fields_by_name[
        "cloud_provider_deprecated"
    ]._serialized_options = b"\030\001"
    _REGION._serialized_start = 77
    _REGION._serialized_end = 358
    _REGION_CLOUDPROVIDER._serialized_start = 263
    _REGION_CLOUDPROVIDER._serialized_end = 358
# @@protoc_insertion_point(module_scope)
