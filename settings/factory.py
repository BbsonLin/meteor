import os
from typing import Dict
from packages.io.reader import JsonReader
from .config import AppConfig, DatabaseConfig, LoggerConfig
from .config import ConfigEnv, APP_CONFIG_NAME, FILENAME_FORMATTER

"""
設定檔
"""


class AppConfigFactory(object):
    @classmethod
    def load(cls, config_name: str, default: ConfigEnv) -> AppConfig:
        # Read app config environment and load config json file.
        app_env: str = os.environ.get(config_name, default.value)
        filename = FILENAME_FORMATTER.format(env=app_env)
        proj_path = os.path.dirname(os.path.dirname(__file__))
        config_path = os.path.abspath(os.path.join(proj_path, filename))
        config_dict = JsonReader.load(config_path)
        # from dictionary to dataclass.
        return AppConfig.from_dict(config_dict)

