import re
from typing import Any, Optional

def is_email(email: str) -> bool:
    """Validate standard email address format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def is_non_empty_string(value: Any) -> bool:
    """Check if input is a string and not empty after whitespace trim."""
    return isinstance(value, str) and bool(value.strip())

def is_valid_int(value: Any, min_val: Optional[int] = None, max_val: Optional[int] = None) -> bool:
    """Check if value is integer and within optional bounds."""
    if not isinstance(value, int) or isinstance(value, bool):
        return False
    if min_val is not None and value < min_val:
        return False
    if max_val is not None and value > max_val:
        return False
    return True

def validate_schema(data: dict, required_keys: list[str]) -> bool:
    """Check if all required keys are present in dict."""
    return all(key in data for key in required_keys)

def sanitize_input(value: str) -> str:
    """Remove dangerous characters from strings."""
    return re.sub(r'[^a-zA-Z0-9\s]', '', value)