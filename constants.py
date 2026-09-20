"""Global constant definitions for python-utils-41 application."""

import os
from enum import Enum
from typing import Final

# Application Metadata
APP_NAME: Final[str] = "python-utils-41"
APP_VERSION: Final[str] = "1.4.0"

# Default Timeout & Retry Configurations
DEFAULT_TIMEOUT_SECONDS: Final[int] = 30
DEFAULT_MAX_RETRIES: Final[int] = 3
DEFAULT_BACKOFF_FACTOR: Final[float] = 1.5

# File and Data Buffering Limits
MAX_FILE_SIZE_BYTES: Final[int] = 10 * 1024 * 1024  # 10 MB
DEFAULT_CHUNK_SIZE: Final[int] = 8192  # 8 KB

# Status Enums
class ProcessingStatus(str, Enum):
    """Standardized processing lifecycle status flags."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"

# Common Regex Patterns
EMAIL_REGEX_PATTERN: Final[str] = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
SLUG_REGEX_PATTERN: Final[str] = r"^[a-z0-9]+(?:-[a-z0-9]+)*$"

# Environment Defaults Helper
def get_env_bool(key: str, default: bool = False) -> bool:
    """Parse environment variable into boolean flag safely."""
    val = os.getenv(key)
    if val is None:
        return default
    return val.strip().lower() in ("true", "1", "yes", "on")
