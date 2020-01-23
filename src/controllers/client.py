from sqlalchemy.orm import joinedload

from src.controllers import ApiController
from src.database import db
from src.models.client import Client
from src.schemas.client_schema import ClientSchema
from src.services.cache import CacheService


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
    def get(self, request_data):
        client_id = request_data.get('client_id')

        cache_svc = CacheService()
        command = cache_svc.get_command(client_id)

        print(command)
        return self.response(command)

    def post(self, request_data):
        client_id = request_data.get('client_id')

        client = Client.query.options(joinedload('commands')).get(client_id)

        command_data = {
            'name': request_data.get('name'),
            'params': request_data.get('params')
        }

        cache_svc = CacheService()
        cache_svc.set_command(client_id, command_data)

        data = (f'Queued [{command_data["name"]}] command for [{client.name}] '
                f'with following params:\n{command_data["params"]}')
        return self.response(data)
