import os
import re
from typing import Final

# general application constants and regex patterns

APP_NAME: Final[str] = "python-utils-41"
VERSION: Final[str] = "1.0.0"

# pattern for standard email validation
EMAIL_REGEX: Final[re.Pattern] = re.compile(
    r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
)

# default timeout configuration for network operations
DEFAULT_TIMEOUT: Final[int] = 30

# directory configuration
BASE_DIR: Final[str] = os.path.dirname(os.path.abspath(__file__))
LOG_DIR: Final[str] = os.path.join(BASE_DIR, "logs")

# common status codes used across utility modules
STATUS_SUCCESS: Final[int] = 200
STATUS_ERROR: Final[int] = 500
STATUS_UNAUTHORIZED: Final[int] = 401

# environment variable keys
ENV_VAR_DEBUG: Final[str] = "DEBUG_MODE"
ENV_VAR_API_KEY: Final[str] = "APP_API_KEY"

# list of supported file extensions for processors
SUPPORTED_EXTENSIONS: Final[tuple] = (".json", ".yaml", ".yml", ".csv")