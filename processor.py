"""Safe data processing utilities with robust error handling for edge cases."""

import math
from typing import Any, Optional, Union


def safe_cast(
    val: Any, target_type: type, default: Optional[Any] = None
) -> Any:
    """Safely cast value to target_type, returning default on edge case failures."""
    if val is None:
        return default
    try:
        if target_type in (int, float) and isinstance(val, (int, float, str)):
            parsed = float(val)
            if math.isnan(parsed) or math.isinf(parsed):
                return default
        return target_type(val)
    except (ValueError, TypeError, OverflowError):
        return default


def safe_divide(
    numerator: Union[int, float],
    denominator: Union[int, float],
    default: Union[int, float] = 0.0,
) -> Union[int, float]:
    """Safely divide numbers, handling division by zero, NaN, and inf values."""
    try:
        num = float(numerator)
        den = float(denominator)
        if den == 0.0 or math.isnan(num) or math.isnan(den) or math.isinf(num) or math.isinf(den):
            return default
        return num / den
    except (ValueError, TypeError, OverflowError):
        return default


def deep_get(
    data: Any, path: str, default: Optional[Any] = None, delimiter: str = "."
) -> Any:
    """Safely retrieve nested dict/list attributes handling invalid path/index edge cases."""
    if not path or not isinstance(path, str):
        return default

    keys = path.split(delimiter)
    current = data

    for key in keys:
        if isinstance(current, dict):
            current = current.get(key, default)
        elif isinstance(current, (list, tuple)):
            try:
                idx = int(key)
                if 0 <= idx < len(current):
                    current = current[idx]
                else:
                    return default
            except (ValueError, TypeError):
                return default
        else:
            return default

        if current is default:
            break

    return current
