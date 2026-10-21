import json
import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

def safe_load_json(file_path: str) -> Optional[Dict[str, Any]]:
    """Safely load and parse JSON from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Failed to load JSON from {file_path}: {e}")
        return None

def chunk_list(data: list, size: int):
    """Split a list into smaller chunks."""
    for i in range(0, len(data), size):
        yield data[i:i + size]

def dict_get_nested(data: Dict, keys: str, default: Any = None) -> Any:
    """Access nested dictionary values using dot notation."""
    parts = keys.split('.')
    current = data
    try:
        for part in parts:
            current = current[part]
        return current
    except (KeyError, TypeError):
        return default

def normalize_string(value: str) -> str:
    """Strip whitespace and lowercase a string."""
    if not isinstance(value, str):
        return ""
    return value.strip().lower()