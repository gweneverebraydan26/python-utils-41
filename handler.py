import json
import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

def safe_json_load(data: str, default: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Parses JSON string or returns a default dict."""
    try:
        return json.loads(data)
    except (json.JSONDecodeError, TypeError) as e:
        logger.error(f"failed to parse json: {e}")
        return default or {}

def chunk_list(data: list, size: int):
    """Yield successive chunks from a list."""
    for i in range(0, len(data), size):
        yield data[i:i + size]

def dict_get_nested(data: Dict, path: str, delimiter: str = '.') -> Any:
    """Retrieve value from nested dictionary using path string."""
    keys = path.split(delimiter)
    value = data
    try:
        for key in keys:
            value = value[key]
        return value
    except (KeyError, TypeError):
        return None

def slugify_string(text: str) -> str:
    """Convert string to simple lowercase slug."""
    return "-".join(text.lower().split()).replace("_", "-")

def ensure_list(value: Any) -> list:
    """Force input into a list format."""
    if value is None:
        return []
    return value if isinstance(value, list) else [value]