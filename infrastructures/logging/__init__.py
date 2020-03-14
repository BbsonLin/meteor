from settings import app_config
from .factory import MeteorLogger


meteor_logger = MeteorLogger.create(app_config)
