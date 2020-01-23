from datetime import datetime
from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import relationship
from src.database import db, JsonEncodedDict

class Client(db.Model):
    __tablename__ = 'client'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    created = db.Column(db.DateTime(), default=func.now())
    last_connection = db.Column(db.DateTime(), default=func.now(), onupdate=datetime.now)

    def __repr__(self):
        return f'<Client(id, {self.name})>'


class ClientCommand(db.Model):
    __tablename__ = 'client_command'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    parameters = db.Column(JsonEncodedDict())
    client_id = db.Column(db.Integer(), ForeignKey('client.id'))

    client = relationship('Client', backref='commands', cascade='all')

    def __repr__(self):
        return f'<ClientCommand(id, {self.client_id}, {self.name})>'
