import os
from flask import Flask

from src.database import db
from src.routes import client as client_api


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py')
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    routes = [client_api]
    for route in routes:
        app.register_blueprint(route.get_blueprint())

    @app.route('/')
    def index():
        return '<div><strong>SuervreuS</strong><br><p>An IoT command processing service</p></div>'

    db.init_app(app)

    return app