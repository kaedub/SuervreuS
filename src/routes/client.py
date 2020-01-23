from flask import Blueprint

from src.base import JsonEndpoint
from src.controllers import ClientController, ClientCommandController

def get_blueprint():
    bp = Blueprint('command_api', __name__)

    client_view = JsonEndpoint.as_view('client', ClientController)
    bp.add_url_rule('/client', view_func=client_view, methods=['POST'])
    bp.add_url_rule('/client/<int:client_id>', view_func=client_view, methods=['GET', 'PUT'])

    command_view = JsonEndpoint.as_view('client_command', ClientCommandController)
    bp.add_url_rule('/client/<int:client_id>/command',view_func=command_view, methods=['GET', 'POST'])

    return bp