from .common import Config


class DevConfig(Config):
    ENV = "development"
    DEBUG = True
    SERVER_PORT = 8000
