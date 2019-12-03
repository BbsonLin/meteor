from settings import app_config
from .console import ConsoleLogger


console_logger = ConsoleLogger.create(app_config)
