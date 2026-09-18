import re
from typing import Any, Optional

def is_valid_email(email: str) -> bool:
    """Check if string is a valid email format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def is_positive_integer(value: Any) -> bool:
    """Check if input is an integer greater than zero."""
    return isinstance(value, int) and value > 0

def validate_length(text: str, min_len: int, max_len: Optional[int] = None) -> bool:
    """Check if string length is within specified bounds."""
    if not isinstance(text, str):
        return False
    if max_len is not None:
        return min_len <= len(text) <= max_len
    return len(text) >= min_len

def is_non_empty_string(value: Any) -> bool:
    """Check if input is a string with content."""
    return isinstance(value, str) and len(value.strip()) > 0

def validate_choice(value: Any, options: list) -> bool:
    """Check if value exists within provided choices."""
    return value in options