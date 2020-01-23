from datetime import datetime
from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import relationship
from src.database import db, JsonEncodedDict

class Device(db.Model):
    __tablename__ = 'device'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    created = db.Column(db.DateTime(), default=func.now())
    last_connection = db.Column(db.DateTime(), default=func.now(), onupdate=datetime.now)


class DeviceCommand(db.Model):
    __tablename__ = 'device_command'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    parameters = db.Column(JsonEncodedDict())
    device_id = db.Column(db.Integer(), ForeignKey('device.id'))

    device = relationship('Device', backref='commands', cascade='all')
