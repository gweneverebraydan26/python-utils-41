class UtilityError(Exception):
    """Base exception for python-utils-41."""

class ValidationError(UtilityError):
    """Raised when data fails schema validation."""

class ConfigurationError(UtilityError):
    """Raised for invalid application configuration."""

class ProcessingError(UtilityError):
    """Raised during core operation failures."""

def handle_execution_context(func):
    """Decorator to wrap operations with error handling."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, TypeError) as e:
            raise ValidationError(f"Data validation failed: {str(e)}") from e
        except KeyError as e:
            raise ConfigurationError(f"Missing required configuration: {str(e)}") from e
        except Exception as e:
            # Log unexpected errors here if logging is available
            raise ProcessingError(f"Unexpected error occurred: {str(e)}") from e
    return wrapper

def safe_execute(operation, *args, **kwargs):
    """Functional interface for safe operation execution."""
    try:
        return operation(*args, **kwargs)
    except UtilityError:
        raise
    except Exception as e:
        raise ProcessingError("Core operation failure") from e