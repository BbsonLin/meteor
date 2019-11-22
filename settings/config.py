from enum import Enum
from typing import List
from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin


APP_CONFIG_NAME = "CHEETAH_ENV"
FILENAME_FORMATTER = "{env}.config.json"


class ConfigEnv(Enum):
    DEV = "dev"
    PROD = "prod"


"""
以下是 App 設定檔讀取後轉換成的資料物件 DTO
若有要在 config.json 中新增參數，要記得來這裡添加欄位，否則無法讀取到
"""


@dataclass
class DatabaseConfig(DataClassJsonMixin):
    USERNAME: str
    PASSWORD: str
    PORT: str
    PROTOCOL: str
    HOSTURL: str
    DB_NAME: str


@dataclass
class LoggerConfig(DataClassJsonMixin):
    FILENAME: str
    LOGGER_NAME: str


@dataclass
class AppConfig(DataClassJsonMixin):
    DEBUG: bool
    DATABASE: DatabaseConfig
    ALLOWED_HOSTS: List[str]
    LOGGER: LoggerConfig
    ALLOW_ORIGINS: List[str]
    SECRET_KEY: str
