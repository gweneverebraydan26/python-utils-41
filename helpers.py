import math
from typing import Any, Dict, Optional

def safe_get_nested(data: Optional[Dict[str, Any]], path: str, default: Any = None) -> Any:
    """
    Safely retrieves a value from a nested dictionary using a dot-separated path.
    Handles edge cases such as None inputs, missing keys, or non-dict structures.
    """
    if not path:
        return default
    if data is None or not isinstance(data, dict):
        return default

    keys = path.split('.')
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

def safe_to_float(value: Any, default: float = 0.0) -> float:
    """
    Converts a value to float safely, handling None, infinity strings, and malformed types.
    """
    if value is None:
        return default
    if isinstance(value, (int, float)):
        if math.isnan(value) or math.isinf(value):
            return default
        return float(value)
    try:
        cleaned = str(value).strip()
        if cleaned.lower() in ('inf', '-inf', 'infinity', '-infinity', 'nan'):
            return default
        return float(cleaned)
    except (ValueError, TypeError):
        return default
