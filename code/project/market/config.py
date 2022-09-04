import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '74255dbc4a797485edfba9f74b751e40'

class Development(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///market.db'

class ProductionUtils:
    MYSQL_HOST = os.environ.get('MYSQL_HOST')
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')
    MYSQL_USER = os.environ.get('MYSQL_USER')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
    

class Production(Config):
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{ProductionUtils.MYSQL_USER}:{ProductionUtils.MYSQL_PASSWORD}@{ProductionUtils.MYSQL_HOST}/{ProductionUtils.MYSQL_DATABASE}'