from .common import Config


class ProdConfig(Config):
    ENV = "production"
    DEBUG = False
    SERVER_PORT = 8080
