from typing import Any, Dict, List, Optional, Union
import math


def safe_get(data: Any, keys: List[Union[str, int]], default: Optional[Any] = None) -> Any:
    """Safely retrieve nested values from dictionaries or lists without raising exceptions."""
    if not isinstance(keys, (list, tuple)):
        return default
    
    current = data
    for key in keys:
        if isinstance(current, dict) and isinstance(key, str):
            current = current.get(key, default)
        elif isinstance(current, (list, tuple)) and isinstance(key, int):
            try:
                current = current[key]
            except IndexError:
                return default
        else:
            return default
        
        if current is default:
            break
            
    return current


def safe_divide(numerator: Union[int, float], denominator: Union[int, float], default: Optional[float] = 0.0) -> Optional[float]:
    """Perform division safely handling ZeroDivisionError, TypeError, and NaN/Infinity cases."""
    try:
        num = float(numerator)
        den = float(denominator)
        if den == 0.0 or math.isnan(num) or math.isnan(den):
            return default
        res = num / den
        return res if not math.isinf(res) else default
    except (ValueError, TypeError):
        return default


def parse_bool(value: Any, default: bool = False) -> bool:
    """Robust boolean parser handling string representations and edge cases."""
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    if isinstance(value, str):
        clean_str = value.strip().lower()
        if clean_str in {"true", "1", "yes", "y", "on", "t"}:
            return True
        if clean_str in {"false", "0", "no", "n", "off", "f"}:
            return False
    return default
