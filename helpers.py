import math
from typing import Any, Mapping, Optional, TypeVar, Union

T = TypeVar("T")


def safe_cast(
    val: Any, to_type: type, default: Optional[T] = None
) -> Union[T, Any]:
    """Safely cast a value to a target type with fallback on failure."""
    if val is None:
        return default
    try:
        if to_type is bool and isinstance(val, str):
            clean_val = val.strip().lower()
            if clean_val in ("true", "1", "yes", "on"):
                return True
            if clean_val in ("false", "0", "no", "off"):
                return False
            return default
        return to_type(val)
    except (ValueError, TypeError, OverflowError):
        return default


def get_nested(
    data: Mapping[str, Any], path: str, default: Any = None, delimiter: str = "."
) -> Any:
    """Retrieve nested mapping values safely handling missing keys and invalid types."""
    if not isinstance(data, Mapping) or not path:
        return default

    keys = [k for k in path.split(delimiter) if k]
    current: Any = data

    for key in keys:
        if not isinstance(current, Mapping):
            return default
        try:
            current = current.get(key, default)
        except (AttributeError, TypeError):
            return default

    return current


def safe_divide(
    numerator: Union[int, float],
    denominator: Union[int, float],
    default: float = 0.0,
) -> float:
    """Perform division with zero and overflow edge case handling."""
    try:
        num = float(numerator)
        den = float(denominator)
        if math.isnan(num) or math.isnan(den):
            return default
        return num / den
    except (ZeroDivisionError, TypeError, ValueError, OverflowError):
        return default
