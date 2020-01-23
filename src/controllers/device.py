from sqlalchemy.orm import joinedload

from src.controllers import ApiController
from src.models.device import Device
from src.schemas.device_schema import DeviceSchema

class DeviceController(ApiController):
    def get(self, request_data):
        device_id = request_data.get('device_id')
        device = Device.query.options(joinedload('commands')).get(device_id)

        schema = DeviceSchema()
        data = schema.dump(device)


        # data = {
        #     'id': device.id,
        #     'name': device.name,
        #     'date_created': device.created,
        #     'date_last_connected': device.last_connection,
        #     'commands': [
        #         {'id': cmd.id, 'name': cmd.name, 'parameters': cmd.parameters}
        #         for cmd in device.commands
        #     ]
        # }
        
        return self.response(data)

    def post(self, request_data):
        # deserialize device data

        data = f'Created new device'

        return self.response(data)

class DeviceCommandController(ApiController):
    def post(self, request_data):
        device_id = request_data.get('device_id')
        command = request_data.get('command')
        params = request_data.get('params')

        # set device-command cache

        data = f'Queued {command} command for device {device_id} with following params: {params}'
        return self.response(data)
