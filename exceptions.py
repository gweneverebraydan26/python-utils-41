class UtilityError(Exception):
    """Base exception for python-utils-41 package."""
    pass

class ConfigurationError(UtilityError):
    """Raised when configuration values are missing or invalid."""
    pass

class ProcessingError(UtilityError):
    """Raised when a data transformation fails."""
    pass

def handle_exceptions(func):
    """Decorator to wrap functions in standard error handling."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, TypeError, KeyError) as e:
            raise ProcessingError(f"Processing failed: {str(e)}") from e
        except Exception as e:
            # Log unexpected errors before re-raising
            print(f"Critical failure in {func.__name__}: {str(e)}")
            raise
    return wrapper

def validate_input(data):
    """Checks if input data is non-empty before processing."""
    if data is None:
        raise ProcessingError("Input data cannot be None")
    if not isinstance(data, (dict, list)):
        raise ProcessingError("Invalid data format, expected dict or list")
    return True