import os
from typing import Type, Union
from .common import Config
from .dev import DevConfig
from .prod import ProdConfig

"""
設定檔
"""

config_mappings = {
    ".dev": DevConfig,
    ".prod": ProdConfig,
}
env = os.environ.get("ENV", ".dev")

config: Type[Config] = config_mappings[env]
