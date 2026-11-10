import re
from typing import Any, Optional

def is_email(value: str) -> bool:
    """Validate RFC 5322 compliant email string."""
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_regex, value))

def is_uuid(value: str) -> bool:
    """Validate standard 8-4-4-4-12 UUID format."""
    uuid_regex = r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'
    return bool(re.match(uuid_regex, value))

def is_not_empty(value: Any) -> bool:
    """Verify object is not None or empty."""
    if value is None:
        return False
    if isinstance(value, (str, list, dict, set)):
        return len(value) > 0
    return True

def validate_range(value: int, min_val: int, max_val: int) -> bool:
    """Check if integer falls within inclusive range."""
    return min_val <= value <= max_val

def sanitize_string(value: str) -> str:
    """Remove non-alphanumeric characters from input."""
    return re.sub(r'[^a-zA-Z0-9]', '', value)