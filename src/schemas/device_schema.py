from marshmallow import Schema, fields, validate


class DeviceCommandSchema(Schema):
    id = fields.Integer(allow_none=True, dump_only=True)
    name = fields.String()
    parameters = fields.String(allow_none=True)

class DeviceSchema(Schema):
    id = fields.Integer(allow_none=True, dump_only=True)
    name = fields.String()
    created = fields.DateTime()
    last_connection = fields.DateTime()
    commands = fields.Nested(DeviceCommandSchema, many=True)
