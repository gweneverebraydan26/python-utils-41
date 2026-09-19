class BaseUtilsError(Exception):
    """Base exception for the python-utils-41 package."""

class ConfigurationError(BaseUtilsError):
    """Raised when configuration values are invalid."""

class ValidationError(BaseUtilsError):
    """Raised when input validation fails."""

class ProcessingError(BaseUtilsError):
    """Raised during data transformation or core tasks."""

class ResourceNotFoundError(BaseUtilsError):
    """Raised when a requested resource is missing."""

def handle_exception(e: Exception) -> None:
    """Log and re-raise standard exceptions."""
    if isinstance(e, BaseUtilsError):
        # Standard logging would be initialized here
        raise e
    raise BaseUtilsError(f"An unexpected error occurred: {str(e)}") from e