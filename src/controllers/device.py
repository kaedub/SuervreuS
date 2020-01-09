from src.controllers import ApiController

class DeviceController(ApiController):
    def get(self, request_data):
        device_id = request_data.get('device_id')
        data = f'Your device id is {device_id}'
        meta = {'device_id': device_id}
        return self.response(data, meta)

    def post(self, request_data):
        device_id = request_data.get('id')
        data = f'Your device id is {device_id}'
        meta = {'device_id': device_id}
        return self.response(data, meta)
