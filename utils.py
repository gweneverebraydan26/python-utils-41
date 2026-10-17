import json
from typing import Any, Dict, Optional

def deep_update(source: Dict[Any, Any], overrides: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Recursively updates a dictionary with nested values.
    """
    for key, value in overrides.items():
        if isinstance(value, dict) and value:
            returned = deep_update(source.get(key, {}), value)
            source[key] = returned
        else:
            source[key] = overrides[key]
    return source

def safe_load_json(file_path: str, default: Any = None) -> Any:
    """
    Loads json safely from disk or returns default.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default

def format_data_size(num: int, suffix: str = 'B') -> str:
    """
    Converts bytes into human readable string format.
    """
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"