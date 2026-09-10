import re
from typing import Any, Optional

# Standard regex patterns for validation
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
IP_REGEX = re.compile(
    r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
)


def is_valid_email(email: Any) -> bool:
    """Validate whether the given input is a valid email address structure.

    Args:
        email: The input string or value to validate.

    Returns:
        True if the input is a string and matches the email pattern, False otherwise.
    """
    if not isinstance(email, str):
        return False
    return bool(EMAIL_REGEX.match(email))


def is_valid_ip(ip_address: Any) -> bool:
    """Check if the provided input is a valid IPv4 address.

    Args:
        ip_address: The input string or value to validate.

    Returns:
        True if the input is a valid IPv4 address string, False otherwise.
    """
    if not isinstance(ip_address, str):
        return False
    return bool(IP_REGEX.match(ip_address))


def validate_range(
    value: float, min_val: Optional[float] = None, max_val: Optional[float] = None
) -> bool:
    """Verify if a numeric value falls within an optionally specified range.

    Args:
        value: The number to check.
        min_val: The optional lower bound (inclusive).
        max_val: The optional upper bound (inclusive).

    Returns:
        True if the value is within bounds, False otherwise.
    """
    if min_val is not None and value < min_val:
        return False
    if max_val is not None and value > max_val:
        return False
    return True
