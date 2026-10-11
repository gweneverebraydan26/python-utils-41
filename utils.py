from typing import Any, Dict, List, Optional, Union

def merge_dicts(dict_a: Dict[Any, Any], dict_b: Dict[Any, Any]) -> Dict[Any, Any]:
    """Recursively merge two dictionaries."""
    result = dict_a.copy()
    for key, value in dict_b.items():
        if isinstance(value, dict) and key in result and isinstance(result[key], dict):
            result[key] = merge_dicts(result[key], value)
        else:
            result[key] = value
    return result

def clean_list(items: List[Optional[Any]]) -> List[Any]:
    """Filter out None values from a list."""
    return [item for item in items if item is not None]

def format_bytes(size: int, precision: int = 2) -> str:
    """Convert bytes into a human-readable string format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.{precision}f} {unit}"
        size /= 1024
    return f"{size:.{precision}f} PB"

def get_nested(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    """Retrieve value from nested dict using dot notation."""
    keys = path.split('.')
    current = data
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default