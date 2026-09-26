class UtilityError(Exception):
    """Base exception class for python-utils-41."""
    pass

class ConfigurationError(UtilityError):
    """Raised when configuration constraints are violated."""
    pass

class ValidationError(UtilityError):
    """Raised when input validation fails."""
    pass

def handle_critical_failure(error: Exception, context: str = "") -> None:
    """Standardizes error reporting for module operations."""
    error_msg = f"[CRITICAL] {type(error).__name__} in {context}: {str(error)}"
    print(error_msg)

def validate_resource_access(resource: any) -> None:
    """Checks resource accessibility before execution."""
    if resource is None:
        raise ValidationError("Provided resource is None type")
    if not hasattr(resource, "__iter__") and not isinstance(resource, (int, float)):
        raise ValidationError("Invalid resource format provided for processing")

def safe_execute(func, *args, **kwargs):
    """Execution wrapper to catch and log general utility errors."""
    try:
        return func(*args, **kwargs)
    except (ConfigurationError, ValidationError) as e:
        handle_critical_failure(e, func.__name__)
        raise
    except Exception as e:
        handle_critical_failure(e, "unexpected failure")
        raise UtilityError("An unforeseen error occurred during processing") from e