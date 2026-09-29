import os
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)

def load_config_value(key: str, default: Any = None) -> Any:
    """Retrieves environment configuration with type safety."""
    try:
        value = os.environ.get(key)
        if value is None:
            return default
        return value
    except Exception as e:
        logger.error(f"Unexpected error accessing env var {key}: {e}")
        return default

def parse_int_config(key: str, default: int) -> int:
    """Parses integer configuration values with fallback."""
    raw_value = load_config_value(key)
    if raw_value is None:
        return default
    try:
        return int(raw_value)
    except (ValueError, TypeError):
        logger.warning(f"Invalid integer for {key}: {raw_value}, using default {default}")
        return default

def validate_config_presence(keys: list) -> None:
    """Checks for required environment variables."""
    missing = [k for k in keys if k not in os.environ]
    if missing:
        logger.critical(f"Missing required configuration keys: {', '.join(missing)}")
        raise EnvironmentError(f"Missing configuration: {', '.join(missing)}")

# Application configuration schema
CONFIG_DEFAULTS = {
    "APP_PORT": 8080,
    "DEBUG_MODE": False
}