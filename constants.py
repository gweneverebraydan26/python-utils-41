import enum
from typing import Final, Dict, Any

# general constants for data handling operations
DEFAULT_ENCODING: Final[str] = "utf-8"
CHUNK_SIZE: Final[int] = 4096
MAX_RETRIES: Final[int] = 3

class DataStatus(enum.Enum):
    SUCCESS = "success"
    FAILURE = "failure"
    PENDING = "pending"

# mapping of common content types
CONTENT_TYPES: Final[Dict[str, str]] = {
    "json": "application/json",
    "csv": "text/csv",
    "txt": "text/plain",
    "yaml": "application/x-yaml"
}

def get_timeout_settings(mode: str = "standard") -> int:
    """returns integer timeout duration based on mode."""
    settings = {
        "fast": 5,
        "standard": 30,
        "slow": 120
    }
    return settings.get(mode, 30)

# validation constraints
MIN_PASSWORD_LENGTH: Final[int] = 12
ALLOWED_EXTENSIONS: Final[set] = {"json", "csv", "txt"}