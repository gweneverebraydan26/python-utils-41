import json
from typing import Any, Dict, Optional

def deep_get(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    """
    Retrieves a nested value from a dictionary using dot notation.
    """
    keys = path.split('.')
    val = data
    try:
        for key in keys:
            val = val[key]
        return val
    except (KeyError, TypeError, AttributeError):
        return default

def sanitize_payload(data: Any) -> Any:
    """
    Recursively cleans data to ensure JSON compatibility.
    """
    if isinstance(data, dict):
        return {str(k): sanitize_payload(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [sanitize_payload(i) for i in data]
    elif isinstance(data, (str, int, float, bool)) or data is None:
        return data
    return str(data)

def load_json_file(filepath: str) -> Optional[Dict[str, Any]]:
    """
    Safe loading of configuration or data files.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None