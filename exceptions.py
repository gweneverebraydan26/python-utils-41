class DataHandlingError(Exception):
    """Base exception for data processing errors."""
    pass

class ValidationError(DataHandlingError):
    """Raised when data fails schema validation."""
    pass

class TransformationError(DataHandlingError):
    """Raised when data transformation fails."""
    pass

def handle_data_error(error: Exception, context: str = "") -> None:
    """
    Standardizes logging for data handling exceptions.
    """
    error_type = type(error).__name__
    message = f"[{error_type}] {context}: {str(error)}"
    print(message)  # Simplified for general utility

def validate_not_none(value, field_name: str):
    """
    Ensures a value is not None, raising ValidationError if so.
    """
    if value is None:
        raise ValidationError(f"Field '{field_name}' cannot be null")
    return value