from sqlalchemy.orm import joinedload

from src.controllers import ApiController
from src.database import db
from src.models.device import Device
from src.schemas.device_schema import DeviceSchema

class DeviceController(ApiController):
    def get(self, request_data):
        device_id = request_data.get('device_id')
        device = Device.query.options(joinedload('commands')).get(device_id)

        schema = DeviceSchema()
        data = schema.dump(device)
        
        return self.response(data)

    def post(self, request_data):
        schema = DeviceSchema()
        device = schema.load(request_data)

        db.session.add(device)
        db.session.commit()

        data = schema.dump(device)
        return self.response(data)

class DeviceCommandController(ApiController):
    def post(self, request_data):
        device_id = request_data.get('device_id')
        cmd_name = request_data.get('name')
        params = request_data.get('params')
        data = f'Queued "{cmd_name}" command for device "{device_id}" with following params:\n{params}'
        return self.response(data)
