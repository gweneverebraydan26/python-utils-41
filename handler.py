import json
from typing import Any, Optional, Dict

def safe_json_load(data: str, default: Any = None) -> Any:
    """Parses a string into a python object with fallback."""
    try:
        return json.loads(data)
    except (ValueError, TypeError):
        return default

def deep_get(dictionary: Dict, keys: str, delimiter: str = '.') -> Any:
    """Access nested dictionary keys via string path."""
    parts = keys.split(delimiter)
    current = dictionary
    try:
        for part in parts:
            current = current[part]
        return current
    except (KeyError, TypeError):
        return None

def flatten_dict(d: Dict, parent_key: str = '', sep: str = '_') -> Dict:
    """Flattens a nested dictionary into a single level."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)