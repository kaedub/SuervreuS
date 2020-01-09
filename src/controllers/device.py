from src.controllers import ApiController

class DeviceController(ApiController):
    def get(self, request_data):
        data = {}
        meta = {}
        return self.response(data, meta)

    def post(self, request_data):
        data = {}
        meta = {}
        return self.response(data=data, meta=meta)
