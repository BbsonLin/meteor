from settings import app_config
from .factory import MeteorLogger


meteor_logman = MeteorLogger.create(app_config)
