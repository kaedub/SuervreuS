import os


DATABASE_URL_PREFIX = 'sqlite:///'
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLALCHEMY_DATABASE_URI = DATABASE_URL_PREFIX + os.path.join(PROJECT_ROOT, 'suervreus.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

CLIENT_URL = 'http://localhost:3000'