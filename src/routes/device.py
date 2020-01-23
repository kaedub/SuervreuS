from flask import Blueprint

from src.base import JsonEndpoint
from src.controllers import DeviceController, DeviceCommandController

def get_blueprint():
    bp = Blueprint('command_api', __name__)

    device_view = JsonEndpoint.as_view('device', DeviceController)
    bp.add_url_rule('/device/<int:device_id>', view_func=device_view, methods=['GET', 'POST', 'PUT'])

    command_view = JsonEndpoint.as_view('device_command', DeviceCommandController)
    bp.add_url_rule('/device/<int:device_id>/command/<string:command>', view_func=command_view, methods=['POST'])

    return bp