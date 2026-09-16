from typing import Final, Dict, Any

# Standardized mapping for common data normalization tasks
DEFAULT_ENCODING: Final[str] = 'utf-8'
CHUNK_SIZE: Final[int] = 8192

# Supported types for validation and casting
TYPE_MAPPINGS: Final[Dict[str, Any]] = {
    'int': int,
    'float': float,
    'str': str,
    'bool': bool
}

# Error message templates for uniform logging
ERROR_MSG_INVALID_INPUT: Final[str] = "invalid input data format: {msg}"
ERROR_MSG_MISSING_KEY: Final[str] = "missing mandatory key: {key}"

# Environment status flags
DEBUG_MODE_DEFAULT: Final[bool] = False
MAX_RETRY_ATTEMPTS: Final[int] = 3

def get_type_caster(type_name: str):
    """Retrieve caster function based on string name."""
    return TYPE_MAPPINGS.get(type_name, str)

# Reserved keywords for system data operations
RESERVED_KEYS: Final[list] = ['id', 'created_at', 'updated_at', 'meta']