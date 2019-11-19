from typing import Dict


class IReader(object):

    @classmethod
    def load(cls, path) -> Dict:
        raise NotImplementedError("Please Implemented")
