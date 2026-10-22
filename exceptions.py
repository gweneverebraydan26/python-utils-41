class UtilsError(Exception):
    """Base exception for python-utils-41."""

class ValidationError(UtilsError):
    """Raised when data fails schema validation."""

class ConfigurationError(UtilsError):
    """Raised for invalid application settings."""

class ResourceNotFoundError(UtilsError):
    """Raised when a requested resource is missing."""

def handle_exception(e: Exception) -> None:
    """Centralized error logging for library operations."""
    if isinstance(e, UtilsError):
        print(f"[Library Error] {e.__class__.__name__}: {str(e)}")
    else:
        print(f"[Unexpected Error] {type(e).__name__}: {str(e)}")

def validate_input(data: any) -> bool:
    """Ensure data is not None or empty."""
    if data is None:
        raise ValidationError("Input data cannot be None")
    if hasattr(data, '__len__') and len(data) == 0:
        raise ValidationError("Input data cannot be empty")
    return True

def safe_execute(func, *args, **kwargs):
    """Wrapper to catch and format library exceptions."""
    try:
        return func(*args, **kwargs)
    except UtilsError as e:
        handle_exception(e)
        return None
    except Exception as e:
        handle_exception(e)
        raise