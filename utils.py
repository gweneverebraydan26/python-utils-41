import json
from typing import Any, Dict, Optional

def deep_get(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    """Retrieve nested dictionary value using dot-notation path."""
    keys = path.split('.')
    current = data
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default

def serialize_json(data: Any, indent: int = 4) -> str:
    """Convert python object to formatted json string."""
    try:
        return json.dumps(data, indent=indent, sort_keys=True)
    except (TypeError, ValueError) as e:
        return str(e)

def sanitize_keys(data: Dict[str, Any], prefix: str = 'clean_') -> Dict[str, Any]:
    """Prefix all dictionary keys for consistent output."""
    return {f"{prefix}{k}": v for k, v in data.items()}

def validate_schema(data: Dict[str, Any], required_keys: list) -> bool:
    """Check if all required keys exist in dictionary."""
    return all(key in data for key in required_keys)