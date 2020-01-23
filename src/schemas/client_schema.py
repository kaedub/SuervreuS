from marshmallow import Schema, fields, post_load

from src.models.client import Client, ClientCommand


class ClientCommandSchema(Schema):
    id = fields.Integer(allow_none=True, dump_only=True)
    name = fields.String()
    parameters = fields.Dict(allow_none=True)

    @post_load
    def make_obj(self, data, **kwargs):
        return ClientCommand(**data)


class ClientSchema(Schema):
    id = fields.Integer(allow_none=True, dump_only=True)
    name = fields.String()
    created = fields.DateTime(allow_none=True)
    last_connection = fields.DateTime(allow_none=True)
    commands = fields.Nested(ClientCommandSchema, many=True)

    @post_load
    def make_obj(self, data, **kwargs):
        return Client(**data)
