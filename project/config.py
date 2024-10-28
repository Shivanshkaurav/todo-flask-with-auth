import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', '34c50497a753a93f2bcef41b87')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False