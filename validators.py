from typing import Any, Optional, Union

def validate_email(email: str) -> bool:
    """Validate format of provided email string."""
    if not isinstance(email, str) or "@" not in email:
        return False
    return True

def ensure_int(value: Any, default: int = 0) -> int:
    """Convert input to integer or return default."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

def validate_range(value: Union[int, float], min_val: float, max_val: float) -> bool:
    """Check if number falls within inclusive bounds."""
    return min_val <= value <= max_val

def clean_string(value: Optional[str]) -> str:
    """Strip whitespace and return empty string if None."""
    if value is None:
        return ""
    return str(value).strip()

def validate_non_empty(data: Any) -> bool:
    """Verify data exists and is not empty container."""
    if data is None:
        return False
    return bool(data)