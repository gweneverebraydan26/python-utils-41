class UtilsError(Exception):
    """Base exception for python-utils-41 package."""

class ConfigurationError(UtilsError):
    """Raised when configuration values are invalid."""

class ValidationError(UtilsError):
    """Raised when data validation fails."""

def raise_if_none(value, message="Value cannot be None"):
    """Checks if a value is None and raises ValidationError."""
    if value is None:
        raise ValidationError(message)

def handle_exception(e, logger=None):
    """Standardizes exception logging and re-raising."""
    if logger:
        logger.error(f"Exception caught: {type(e).__name__} - {str(e)}")
    raise e

class ExceptionContext:
    """Context manager to suppress or re-raise errors."""
    def __init__(self, suppress=False):
        self.suppress = suppress

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            if self.suppress:
                return True
            return False
        return True