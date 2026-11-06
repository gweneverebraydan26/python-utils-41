import os
import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

def load_config_value(key: str, default: Optional[Any] = None) -> Any:
    """Retrieves environment configuration with type safety."""
    try:
        value = os.getenv(key)
        if value is None:
            if default is None:
                raise KeyError(f"Missing required configuration: {key}")
            return default
        return value
    except Exception as e:
        logger.error(f"Unexpected error loading config {key}: {str(e)}")
        return default

def parse_int_config(key: str, default: int) -> int:
    """Safely parses an integer configuration value."""
    val = load_config_value(key, str(default))
    try:
        return int(val)
    except (ValueError, TypeError):
        logger.warning(f"Invalid integer for {key}: {val}. Using default: {default}")
        return default

def get_app_settings() -> Dict[str, Any]:
    """Assembles application settings with validation."""
    return {
        "port": parse_int_config("APP_PORT", 8080),
        "timeout": parse_int_config("APP_TIMEOUT", 30),
        "debug": load_config_value("DEBUG", "false").lower() == "true"
    }