import os

from flask import Flask, g

from src.database import db
from src.routes import device as device_api
# from src.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )


    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + SQLALCHEMY_DATABASE_URI
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py')
    else:
        app.config.from_mapping(test_config)

    print('connected to')
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    routes = [device_api]
    for route in routes:
        app.register_blueprint(route.get_blueprint())

    @app.route('/')
    def index():
        return '<div><strong>SuervreuS</strong><br><p>An IoT command processing service</p></div>'

    db.init_app(app)

    return app