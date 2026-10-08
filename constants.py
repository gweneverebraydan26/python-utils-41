import os
import logging
from typing import Final

# Application configuration defaults
DEFAULT_ENCODING: Final[str] = 'utf-8'
CHUNK_SIZE: Final[int] = 8192
MAX_RETRIES: Final[int] = 3

# Environment-based paths with fallback
BASE_DIR: Final[str] = os.path.dirname(os.path.abspath(__file__))
LOG_DIR: Final[str] = os.getenv('LOG_DIR', os.path.join(BASE_DIR, 'logs'))

# Standardized date/time formats
ISO_DATETIME_FORMAT: Final[str] = '%Y-%m-%dT%H:%M:%S%z'
FILE_DATE_FORMAT: Final[str] = '%Y%m%d_%H%M%S'

# Logging configuration defaults
LOG_LEVEL: Final[int] = logging.INFO
LOG_FORMAT: Final[str] = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Timeout settings in seconds
DEFAULT_TIMEOUT: Final[float] = 30.0
HTTP_READ_TIMEOUT: Final[float] = 10.0

# Supported file extensions for processing
SUPPORTED_EXTENSIONS: Final[tuple[str, ...]] = ('.json', '.yaml', '.txt', '.csv')

# Environment identifiers
ENV_PRODUCTION: Final[str] = 'production'
ENV_DEVELOPMENT: Final[str] = 'development'
ENV_TESTING: Final[str] = 'testing'