from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

from src.models.base import Base

class Device(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    name = Column()
    date_created = DateTime(default=datetime.datetime.now())
    last_connection_date = DateTime(default=datetime.datetime.now())
