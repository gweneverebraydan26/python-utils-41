class BaseUtilsError(Exception):
    """Base exception for python-utils-41 package."""
    pass

class ConfigurationError(BaseUtilsError):
    """Raised when configuration validation fails."""
    pass

class ProcessingError(BaseUtilsError):
    """Raised during data transformation failures."""
    def __init__(self, message, original_exception=None):
        super().__init__(message)
        self.original_exception = original_exception

class ValidationError(BaseUtilsError):
    """Raised when inputs do not meet requirements."""
    def __init__(self, field, reason):
        self.field = field
        self.reason = reason
        super().__init__(f"Invalid field '{field}': {reason}")

def handle_exception(e):
    """Centralized error reporting utility."""
    if isinstance(e, BaseUtilsError):
        print(f"[Utils Error] {e.__class__.__name__}: {e}")
    else:
        print(f"[Unexpected Error] {type(e).__name__}: {str(e)}")
    raise e