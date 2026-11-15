"""Validation utilities with edge-case handling for common data types."""

from typing import Any, Dict, Optional, Type, Union


class ValidationError(Exception):
    """Custom exception raised when data validation fails."""
    pass


def validate_numeric_range(
    value: Any,
    min_val: Optional[Union[int, float]] = None,
    max_val: Optional[Union[int, float]] = None,
    allow_none: bool = False,
) -> Union[int, float, None]:
    """Validate and convert numeric input within specified boundaries."""
    if value is None:
        if allow_none:
            return None
        raise ValidationError("Value cannot be None")

    try:
        num = float(value)
    except (ValueError, TypeError) as err:
        raise ValidationError(f"Cannot convert {type(value).__name__} to numeric: {value}") from err

    if min_val is not None and num < min_val:
        raise ValidationError(f"Value {num} is below minimum allowed value of {min_val}")
    if max_val is not None and num > max_val:
        raise ValidationError(f"Value {num} exceeds maximum allowed value of {max_val}")

    if isinstance(value, int) or (isinstance(value, str) and value.isdigit()):
        return int(num)
    return num


def validate_dict_schema(
    data: Any,
    required_keys: Dict[str, Type],
    allow_extra: bool = True,
) -> Dict[str, Any]:
    """Validate key presence and value types in a dictionary structure."""
    if not isinstance(data, dict):
        raise ValidationError(f"Expected dictionary, received {type(data).__name__}")

    missing_keys = [k for k in required_keys if k not in data]
    if missing_keys:
        raise ValidationError(f"Missing required keys: {', '.join(sorted(missing_keys))}")

    invalid_types = []
    for key, expected_type in required_keys.items():
        val = data[key]
        if not isinstance(val, expected_type):
            invalid_types.append(f"'{key}' expected {expected_type.__name__}, got {type(val).__name__}")

    if invalid_types:
        raise ValidationError(f"Schema type mismatches: {'; '.join(invalid_types)}")

    if not allow_extra:
        extra_keys = set(data.keys()) - set(required_keys.keys())
        if extra_keys:
            raise ValidationError(f"Unexpected extra keys found: {', '.join(sorted(extra_keys))}")

    return data
