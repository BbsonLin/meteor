from enum import Enum
from typing import List, Optional
from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin


"""
APP_CONFIG_NAME : 使用在環境變數上，用來讀取寫在環境變數中，要讀取的 Config 用的變數名稱
ConfigEnv: 可以選擇的環境設定檔檔名，如果為 DEV 則讀取 dev 開頭的環境變數。
FILENAME_FORMATTER: 設定檔的檔名格式。
"""


APP_CONFIG_NAME = "CHEETAH_ENV"
FILENAME_FORMATTER = "config.{env}.json"


# Config 不同環境版本的設定檔名
class ConfigEnv(Enum):
    LOCAL = "local"
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
    RDBMS: str
    PYDRIVER: str
    # 測試使用：顯示每次操作的訊息
    ECHO: bool
    # 資料庫的 HOST URL 與 PORT，如果有設定 DSN 則直接採用 DSN
    DB_NAME: Optional[str] = None
    DB_DRIVER: Optional[str] = None
    HOSTURL: Optional[str] = None
    PORT: Optional[str] = None
    DSN: Optional[str] = None

    @property
    def CONNECTION_STRING(self) -> str:
        conn_string: str
        proto: str = "{rdbms}+{pydriver}".format(rdbms=self.RDBMS, pydriver=self.PYDRIVER)
        # 採用 odbc.ini 預設寫好的參數直接讀取
        if self.DSN is not None:
            conn_string = "{proto}://{username}:{paswrd}@{dsn}"
            conn_string = conn_string.format(proto=proto, username=self.USERNAME, paswrd=self.PASSWORD, dsn=self.DSN)
        # 自行設定參數組成字串
        elif self.DSN is None and (self.PORT and self.HOSTURL and self.DB_NAME):
            conn_string = "{proto}://{username}:{paswrd}@{host}:{port}/{dbname}"
            conn_string = conn_string.format(proto=proto,
                                             username=self.USERNAME,
                                             paswrd=self.PASSWORD,
                                             host=self.HOSTURL,
                                             port=self.PORT,
                                             dbname=self.DB_NAME)
            # 如果是 MSSQL，則加入驅動字串
            if self.RDBMS == "mssql" and self.DB_DRIVER:
                conn_string = "{conn}?={driver}".format(conn=conn_string, driver=self.DB_DRIVER)
        else:
            raise Exception("Database Connection String Setting Error !")
        return conn_string


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
