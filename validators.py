from typing import Any, Optional, Union

def validate_email(email: str) -> bool:
    """Validate email string format using basic presence checks."""
    if not isinstance(email, str) or "@" not in email:
        return False
    return len(email.split("@")[1].split(".")) > 1

def validate_range(value: Union[int, float], min_val: float, max_val: float) -> bool:
    """Check if numeric value is within specified bounds."""
    return min_val <= value <= max_val

def sanitize_string(value: Any, default: str = "") -> str:
    """Ensure output is a string, returning default if input is None."""
    if value is None:
        return default
    return str(value).strip()

def is_not_empty(data: Optional[Union[str, list, dict]]) -> bool:
    """Verify that the provided structure is not null or empty."""
    if data is None:
        return False
    return bool(data)

if __name__ == "__main__":
    # Example usage for verification
    assert validate_email("test@example.com") is True
    assert validate_range(50, 0, 100) is True
    assert sanitize_string(None) == ""
    assert is_not_empty([1, 2, 3]) is True