from typing import Optional, Any

class UtilsError(Exception):
    """Base exception for python-utils-41 package."""
    def __init__(self, message: str, code: Optional[int] = None) -> None:
        super().__init__(message)
        self.code = code

class ConfigurationError(UtilsError):
    """Raised when utility configuration is invalid."""
    pass

class ProcessingError(UtilsError):
    """Raised when data processing encounters an error."""
    def __init__(self, message: str, context: Optional[Any] = None) -> None:
        super().__init__(message)
        self.context = context

def raise_if_none(value: Any, name: str) -> None:
    """Validate that a variable is not None, or raise ConfigurationError."""
    if value is None:
        raise ConfigurationError(f"Variable '{name}' must not be None")

def format_exception(exc: Exception) -> str:
    """Convert an exception object into a readable string."""
    return f"{type(exc).__name__}: {str(exc)}"