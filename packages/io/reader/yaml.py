import io
import os
import yaml
from .interface import IReader


class YamlReader(IReader):
    """
    YAML 載入器
    """

    @classmethod
    def load(cls, path):
        with open(path, "r") as f:
            return yaml.safe_load(f.read())
