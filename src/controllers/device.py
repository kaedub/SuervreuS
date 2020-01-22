from src.controllers import ApiController
from src.models.device import Device

class DeviceController(ApiController):
    def get(self, request_data):
        device_id = request_data.get('device_id')

        device = Device.query.get(device_id)
        
        return self.response(data, meta)

    def post(self, request_data):
        device_id = request_data.get('id')

        # deserialize device data

        data = f'Your device id is {device_id}'
        meta = {'device_id': device_id}
        return self.response(data, meta)

class DeviceCommandController(ApiController):
    def post(self, request_data):
        device_id = request_data.get('device_id')
        command = request_data.get('command')
        params = request_data.get('params')

        # set device-command cache

        data = f'Queued {command} command for device {device_id} with following params: {params}'
        return self.response(data)
