from settings import app_config
from .factory import CheetahLogger


cheetah_logger = CheetahLogger.create(app_config)
