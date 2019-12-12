import os
from logging import Logger
from settings import AppConfig
from packages.io.logging import LoggerFactory


class CheetahLogger(object):
    @classmethod
    def create(cls, config: AppConfig) -> Logger:
        # Read config filename and path
        proj_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        filename: str = config.LOGGER.FILENAME
        logging_yaml: str = "{name}.conf.yml".format(name=filename)
        logging_config = os.path.abspath(os.path.join(proj_path, logging_yaml))
        # Load config
        factory = LoggerFactory()
        factory.load_config(logging_config)
        logger = factory.get_logger(config.LOGGER.LOGGER_NAME)
        return logger
