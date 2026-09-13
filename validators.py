import json
import re

# Regular expressions for basic email and phone validation
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
PHONE_REGEX = re.compile(r"^\+?[1-9]\d{1,14}$")  # E.164 format


def is_valid_email(email: str) -> bool:
    """Check if the provided string is a valid email address."""
    if not isinstance(email, str):
        return False
    return bool(EMAIL_REGEX.match(email))


def is_valid_phone(phone: str) -> bool:
    """Check if the provided string is a valid E.164 phone number."""
    if not isinstance(phone, str):
        return False
    # Strip spaces and dashes for checking
    cleaned = phone.replace(" ", "").replace("-", "")
    return bool(PHONE_REGEX.match(cleaned))


def is_valid_json(json_str: str) -> bool:
    """Verify if a string is a valid JSON document."""
    if not isinstance(json_str, str):
        return False
    try:
        json.loads(json_str)
        return True
    except (ValueError, TypeError):
        return False