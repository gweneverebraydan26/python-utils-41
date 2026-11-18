import typing

def validate_numeric_input(value: typing.Any, min_val: float = 0.0, max_val: float = float('inf')) -> float:
    """Validates that the input is a number within a specified range."""
    try:
        num = float(value)
    except (ValueError, TypeError):
        raise ValueError(f"Input '{value}' is not a valid numeric type.")

    if not (min_val <= num <= max_val):
        raise ValueError(f"Value {num} out of bounds [{min_val}, {max_val}].")
    
    return num

def safe_dictionary_access(data: dict, key: str, default: typing.Any = None) -> typing.Any:
    """Safely retrieves a value from a dictionary with fallback."""
    if not isinstance(data, dict):
        return default
    return data.get(key, default)

def sanitize_string_input(value: typing.Any, max_length: int = 255) -> str:
    """Sanitizes and truncates string input for data safety."""
    if value is None:
        return ""
    
    string_value = str(value).strip()
    if len(string_value) > max_length:
        return string_value[:max_length]
    
    return string_value