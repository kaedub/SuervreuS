import os


SQLITE_PREFIX = 'sqlite:///'
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLALCHEMY_DATABASE_URI = SQLITE_PREFIX + os.path.join(PROJECT_ROOT, 'suervreus.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
