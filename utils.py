import logging
from typing import Any, Optional, Union

logger = logging.getLogger(__name__)

def safe_divide(a: Union[int, float], b: Union[int, float]) -> Optional[float]:
    """Performs safe division with zero handling."""
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        logger.error("attempted division by zero")
        return None
    except (TypeError, ValueError):
        logger.error("invalid non-numeric input provided")
        return None

def get_nested_key(data: dict, keys: list, default: Any = None) -> Any:
    """Safely retrieves values from deep nested dictionary."""
    if not isinstance(data, dict):
        return default
    
    current = data
    try:
        for key in keys:
            if not isinstance(current, dict) or key not in current:
                return default
            current = current[key]
        return current
    except Exception as e:
        logger.error(f"unexpected lookup error: {e}")
        return default

def parse_int_safe(value: Any, fallback: int = 0) -> int:
    """Converts input to int with robust fallbacks."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return fallback