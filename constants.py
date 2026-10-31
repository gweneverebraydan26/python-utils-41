"""Module defining global application constants, defaults, and formats."""

from enum import Enum, unique
from typing import Final, Dict, Any

# General Application Metadata
APP_NAME: Final[str] = "python-utils-41"
DEFAULT_ENCODING: Final[str] = "utf-8"
BUFFER_SIZE: Final[int] = 8192

# Timeouts and Limits (in seconds/units)
DEFAULT_TIMEOUT: Final[float] = 30.0
MAX_RETRIES: Final[int] = 3
BACKOFF_FACTOR: Final[float] = 1.5

# Standard Date & Time Formats
ISO_DATETIME_FORMAT: Final[str] = "%Y-%m-%dT%H:%M:%SZ"
LOG_DATETIME_FORMAT: Final[str] = "%Y-%m-%d %H:%M:%S"
SIMPLE_DATE_FORMAT: Final[str] = "%Y-%m-%d"

# File Processing Extensions
SUPPORTED_TEXT_EXTENSIONS: Final[tuple] = (".txt", ".md", ".json", ".csv", ".yaml", ".yml")
SUPPORTED_IMAGE_EXTENSIONS: Final[tuple] = (".png", ".jpg", ".jpeg", ".webp", ".gif")


@unique
class Environment(str, Enum):
    """Supported execution environments."""

    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
    TESTING = "testing"


@unique
class LogLevel(str, Enum):
    """Standard logging level strings."""

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


# Default System Configuration Values
DEFAULT_CONFIG: Final[Dict[str, Any]] = {
    "env": Environment.DEVELOPMENT.value,
    "debug": False,
    "log_level": LogLevel.INFO.value,
    "timeout": DEFAULT_TIMEOUT,
    "max_retries": MAX_RETRIES,
    "encoding": DEFAULT_ENCODING,
}
