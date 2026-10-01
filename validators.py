"""Validation utilities for common data structures and input formats."""

import re
from typing import Any, Container, Dict, List, Optional, Union

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
URL_REGEX = re.compile(r"^https?://[^\s/$.?#].[^\s]*$", re.IGNORECASE)


def is_valid_email(email: str) -> bool:
    """Validate whether a given string is a correctly formatted email address.

    Args:
        email: The string to check for email format.

    Returns:
        True if the email format is valid, False otherwise.
    """
    if not isinstance(email, str):
        return False
    return bool(EMAIL_REGEX.match(email.strip()))


def is_valid_url(url: str) -> bool:
    """Check if a string is a valid HTTP or HTTPS URL.

    Args:
        url: The string candidate to evaluate.

    Returns:
        True if the URL matches standard HTTP/HTTPS syntax.
    """
    if not isinstance(url, str):
        return False
    return bool(URL_REGEX.match(url.strip()))


def is_in_range(
    value: Union[int, float],
    min_val: Optional[Union[int, float]] = None,
    max_val: Optional[Union[int, float]] = None,
) -> bool:
    """Verify if a numeric value falls within an optional range.

    Args:
        value: The number to test.
        min_val: Minimum acceptable boundary (inclusive).
        max_val: Maximum acceptable boundary (inclusive).

    Returns:
        True if value satisfies boundary conditions, False otherwise.
    """
    if not isinstance(value, (int, float)):
        return False
    if min_val is not None and value < min_val:
        return False
    if max_val is not None and value > max_val:
        return False
    return True


def validate_dict_keys(data: Dict[str, Any], required_keys: Container[str]) -> List[str]:
    """Find missing required keys in a given dictionary.

    Args:
        data: The dictionary to inspect.
        required_keys: A collection of expected key names.

    Returns:
        A list of missing key names.
    """
    if not isinstance(data, dict):
        return list(required_keys)
    return [key for key in required_keys if key not in data]
