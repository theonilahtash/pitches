import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:moringa1234@localhost/pitch'


class ProdConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:moringa1234@localhost/pitch'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}