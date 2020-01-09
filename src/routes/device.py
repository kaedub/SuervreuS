from flask import Blueprint

from src.base import JsonEndpoint
from src.controllers import DeviceController

def get_blueprint():
    bp = Blueprint('command_api', __name__)

    device_view = JsonEndpoint.as_view('device', DeviceController)
    bp.add_url_rule('/device/<int:device_id>', view_func=device_view, methods=['GET', 'POST', 'PUT'])

    return bp