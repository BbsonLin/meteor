import io
import os
import json
from .interface import IReader


class JsonReader(IReader):
    """
    Json 載入器
    """

    @classmethod
    def load(cls, path):
        # io.open 支援 encoding 編碼
        with io.open(path, "r", encoding="utf-8") as f:
            return json.load(f)
