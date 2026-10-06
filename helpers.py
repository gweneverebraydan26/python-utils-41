import json
import logging
from typing import Any, Dict, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def safe_json_load(data: str, default: Any = None) -> Any:
    """Parse json string with fallback to default."""
    try:
        return json.loads(data)
    except (json.JSONDecodeError, TypeError):
        return default

def get_nested(data: Dict, path: str, default: Any = None) -> Any:
    """Access nested dictionary values using dot notation."""
    keys = path.split('.')
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

def chunk_list(items: list, size: int):
    """Split a list into chunks of a given size."""
    if size <= 0:
        raise ValueError("chunk size must be positive")
    for i in range(0, len(items), size):
        yield items[i:i + size]

def sanitize_dict(data: Dict) -> Dict:
    """Remove keys with None values from dictionary."""
    return {k: v for k, v in data.items() if v is not None}
