from sqlalchemy.orm import joinedload

from src.controllers import ApiController
from src.database import db
from src.models.client import Client
from src.schemas.client_schema import ClientSchema

class ClientController(ApiController):
    def get(self, request_data):
        client_id = request_data.get('client_id')
        client = Client.query.options(joinedload('commands')).get(client_id)

        schema = ClientSchema()
        data = schema.dump(client)
        
        return self.response(data)

    def post(self, request_data):
        schema = ClientSchema()
        client = schema.load(request_data)

        db.session.add(client)
        db.session.commit()

        data = schema.dump(client)
        return self.response(data)

class ClientCommandController(ApiController):
    def post(self, request_data):
        client_id = request_data.get('client_id')
        cmd_name = request_data.get('name')
        params = request_data.get('params')

        client = Client.query.options(joinedload('commands')).get(client_id)

        data = f'Queued [{cmd_name}] command for [{client.name}] with following params:\n{params}'
        return self.response(data)
