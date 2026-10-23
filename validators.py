import re
from typing import Any, Optional

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

def is_valid_email(email: Any) -> bool:
    """Validate string format for email addresses."""
    if not isinstance(email, str):
        return False
    return bool(EMAIL_REGEX.match(email))

def is_non_empty_string(value: Any) -> bool:
    """Check if value is a string and contains non-whitespace."""
    return isinstance(value, str) and bool(value.strip())

def ensure_list(value: Any) -> list:
    """Convert single items to lists, leave lists unchanged."""
    if value is None:
        return []
    if isinstance(value, (list, tuple, set)):
        return list(value)
    return [value]

def validate_range(value: int, min_val: int, max_val: int) -> bool:
    """Check if integer falls within inclusive boundaries."""
    return isinstance(value, int) and min_val <= value <= max_val

def safe_get(data: dict, key: str, default: Any = None) -> Any:
    """Retrieve value from dict with fallback."""
    return data.get(key, default) if isinstance(data, dict) else default