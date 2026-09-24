from typing import Optional, Any

class BaseUtilsError(Exception):
    """Base exception for the python-utils-41 package."""
    def __init__(self, message: str, code: Optional[int] = None) -> None:
        super().__init__(message)
        self.code = code

class ConfigurationError(BaseUtilsError):
    """Raised when a configuration value is invalid or missing."""
    pass

class ProcessingError(BaseUtilsError):
    """Raised when data processing operations fail."""
    pass

def raise_if_none(value: Any, name: str) -> None:
    """Raise ProcessingError if the provided value is None.

    Args:
        value: The object to check.
        name: The name of the variable for the error message.
    """
    if value is None:
        raise ProcessingError(f"Variable '{name}' cannot be None")

def validate_code(code: Optional[int]) -> bool:
    """Validate if a status code is within the acceptable range.

    Args:
        code: The status code to validate.

    Returns:
        bool: True if the code is positive, False otherwise.
    """
    if code is None:
        return False
    return code > 0