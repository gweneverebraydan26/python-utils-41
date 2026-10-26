import os
from typing import Final

# Application path configurations
BASE_DIR: Final[str] = os.path.dirname(os.path.abspath(__file__))
LOG_DIR: Final[str] = os.path.join(BASE_DIR, 'logs')

# Default operation timeouts
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Supported data formats
SUPPORTED_EXTENSIONS: Final[set] = {'.json', '.yaml', '.csv', '.txt'}

# Environment defaults
ENV_PREFIX: Final[str] = 'PYUTILS'
DEBUG_MODE: Final[bool] = os.getenv(f'{ENV_PREFIX}_DEBUG', 'False') == 'True'

# System messages
ERROR_PREFIX: Final[str] = '[ERROR]'
SUCCESS_PREFIX: Final[str] = '[SUCCESS]'

def get_config_path(filename: str) -> str:
    """Return full path for configuration files."""
    return os.path.join(BASE_DIR, 'config', filename)

def is_supported(filepath: str) -> bool:
    """Check if the file extension is supported."""
    _, ext = os.path.splitext(filepath)
    return ext.lower() in SUPPORTED_EXTENSIONS