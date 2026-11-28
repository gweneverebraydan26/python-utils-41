import enum
from typing import Dict, Any

class DataFormat(enum.Enum):
    """Supported serialization formats for data processing."""
    JSON = "json"
    YAML = "yaml"
    CSV = "csv"

class ConfigDefaults:
    """Default application configuration constants."""
    MAX_RETRIES: int = 3
    TIMEOUT_SECONDS: float = 30.0
    CHUNK_SIZE: int = 1024
    ENCODING: str = "utf-8"

def get_environment_defaults() -> Dict[str, Any]:
    """Return baseline environment configuration mapping."""
    return {
        "retries": ConfigDefaults.MAX_RETRIES,
        "timeout": ConfigDefaults.TIMEOUT_SECONDS,
        "chunk_size": ConfigDefaults.CHUNK_SIZE,
        "encoding": ConfigDefaults.ENCODING
    }

# Status codes for internal utility operations
STATUS_SUCCESS: int = 200
STATUS_ERROR: int = 500
STATUS_INVALID: int = 400