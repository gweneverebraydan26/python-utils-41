"""General data validation utilities for Python applications."""

import re
from typing import Any, Dict, List, Optional, Union

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
URL_REGEX = re.compile(
    r"^(?:http|ftp)s?://"  # http:// or https://
    r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
    r"localhost|"
    r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
    r"(?::\d+)?"
    r"(?:/?|[/?]\S+)$",
    re.IGNORECASE,
)


def is_valid_email(email: str) -> bool:
    """Validate if the given string is a properly formatted email address.

    Args:
        email: String representation of the email to check.

    Returns:
        True if valid email format, False otherwise.
    """
    if not isinstance(email, str):
        return False
    return bool(EMAIL_REGEX.match(email.strip()))


def is_valid_url(url: str) -> bool:
    """Check whether a provided string matches standard HTTP/HTTPS/FTP URL structure.

    Args:
        url: The URL string to validate.

    Returns:
        True if the URL format is valid, False otherwise.
    """
    if not isinstance(url, str):
        return False
    return bool(URL_REGEX.match(url.strip()))


def validate_range(
    value: Union[int, float],
    min_val: Optional[Union[int, float]] = None,
    max_val: Optional[Union[int, float]] = None,
) -> bool:
    """Ensure a numerical value falls within an optional minimum and maximum range.

    Args:
        value: Number to check.
        min_val: Minimum acceptable value inclusive.
        max_val: Maximum acceptable value inclusive.

    Returns:
        True if value falls within specified range boundaries.
    """
    if min_val is not None and value < min_val:
        return False
    if max_val is not None and value > max_val:
        return False
    return True


def has_required_keys(data: Dict[str, Any], keys: List[str]) -> bool:
    """Verify that all specified keys exist in a dictionary.

    Args:
        data: The dictionary to check.
        keys: List of key names that must be present.

    Returns:
        True if all required keys are present in dictionary, False otherwise.
    """
    if not isinstance(data, dict):
        return False
    return all(k in data for k in keys)
