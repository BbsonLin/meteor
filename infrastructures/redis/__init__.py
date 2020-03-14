from settings import app_config
from .adapter import RedisAdapter

redis_adapter = RedisAdapter(app_config.REDIS_CONF)
