import os
import logging
from typing import Any, Final

# Configure logger for module diagnostics
logger = logging.getLogger(__name__)

def get_env_constant(key: str, default: Any = None) -> Any:
    """
    Safely retrieve environment variables with type fallback.
    Handles missing keys or empty environment configurations.
    """
    try:
        value = os.environ.get(key)
        if value is None:
            if default is None:
                raise KeyError(f"Environment variable '{key}' is missing")
            return default
        return value
    except Exception as e:
        logger.error(f"Unexpected error retrieving constant {key}: {e}")
        return default

# Application-wide default constraints
MAX_RETRY_ATTEMPTS: Final[int] = 3
TIMEOUT_SECONDS: Final[int] = 30
DEFAULT_ENCODING: Final[str] = "utf-8"

# Validate critical system configuration
if not isinstance(MAX_RETRY_ATTEMPTS, int) or MAX_RETRY_ATTEMPTS < 0:
    logger.warning("Invalid MAX_RETRY_ATTEMPTS, resetting to 0")
    MAX_RETRY_ATTEMPTS = 0

class ConfigError(Exception):
    """
    Custom exception for configuration failures.
    """
    pass

def validate_config(config_dict: dict) -> bool:
    """
    Ensure required keys exist within the config object.
    """
    required = ['VERSION', 'DEBUG_MODE']
    for key in required:
        if key not in config_dict:
            raise ConfigError(f"Missing required configuration: {key}")
    return True