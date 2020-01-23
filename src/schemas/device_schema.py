from marshmallow import Schema, fields, post_load

from src.models.device import Device, DeviceCommand


class DeviceCommandSchema(Schema):
    id = fields.Integer(allow_none=True, dump_only=True)
    name = fields.String()
    parameters = fields.Dict(allow_none=True)

    @post_load
    def make_obj(self, data, **kwargs):
        return DeviceCommand(**data)


class DeviceSchema(Schema):
    id = fields.Integer(allow_none=True, dump_only=True)
    name = fields.String()
    created = fields.DateTime(allow_none=True)
    last_connection = fields.DateTime(allow_none=True)
    commands = fields.Nested(DeviceCommandSchema, many=True)

    @post_load
    def make_obj(self, data, **kwargs):
        return Device(**data)
