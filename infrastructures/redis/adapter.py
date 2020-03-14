import json
from redis import StrictRedis, ConnectionPool
from settings import app_config, RedisConfig


class RedisAdapter(object):
    def __init__(self, config: RedisConfig) -> None:
        self._pool = ConnectionPool(host=config.HOSTURL, port=config.PORT, db=config.DBNO, password=config.PWD, decode_responses=True)
        self._redis = StrictRedis(connection_pool=self._pool)

    @property
    def instance(self) -> StrictRedis:
        return self._redis
