from .factory import AppConfigFactory
from .config import ConfigEnv, APP_CONFIG_NAME, FILENAME_FORMATTER
from .config import AppConfig, DatabaseConfig

# Initialized
app_config: AppConfig = AppConfigFactory.load(APP_CONFIG_NAME, ConfigEnv.LOCAL)
