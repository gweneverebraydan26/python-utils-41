import re
from typing import Any, Optional

class DataValidator:
    """Utility class for common data structure validation."""

    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Check if string is a valid email format."""
        if not isinstance(email, str):
            return False
        return bool(DataValidator.EMAIL_REGEX.match(email))

    @staticmethod
    def validate_non_empty_string(value: Any) -> bool:
        """Verify input is a non-empty string."""
        return isinstance(value, str) and len(value.strip()) > 0

    @staticmethod
    def validate_range(value: int, min_val: int, max_val: int) -> bool:
        """Ensure integer is within inclusive boundaries."""
        return isinstance(value, int) and min_val <= value <= max_val

def sanitize_input(data: str) -> str:
    """Basic strip and cleaning for user input."""
    if not isinstance(data, str):
        return ""
    return data.strip().replace("<", "&lt;").replace(">", "&gt;")

# Helper instances for cleaner access
validator = DataValidator()