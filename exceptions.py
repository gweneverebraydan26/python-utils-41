class UtilityError(Exception):
    """Base exception for python-utils-41"""
    pass

class DataProcessingError(UtilityError):
    """Raised when data transformation fails"""
    pass

class ValidationError(UtilityError):
    """Raised when data validation fails"""
    pass

def raise_if_invalid(data: dict, schema: list) -> None:
    """Validates dictionary keys against schema list"""
    missing = [key for key in schema if key not in data]
    if missing:
        raise ValidationError(f"Missing required keys: {', '.join(missing)}")

def safe_extract(data: dict, key: str, default=None):
    """Safe key retrieval from nested dictionaries"""
    try:
        return data.get(key, default)
    except AttributeError:
        raise DataProcessingError(f"Invalid data format: expected dict, got {type(data).__name__}")