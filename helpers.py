import logging
from typing import Any, Optional, Callable

logger = logging.getLogger(__name__)

def safe_execute(func: Callable, *args: Any, default: Any = None, **kwargs: Any) -> Any:
    """
    Executes a function safely with comprehensive error handling.
    Returns the default value if an exception occurs.
    """
    try:
        return func(*args, **kwargs)
    except (ValueError, TypeError, KeyError, IndexError) as e:
        logger.warning(f"Standard edge case encountered in {func.__name__}: {e}")
        return default
    except Exception as e:
        logger.error(f"Unexpected system failure in {func.__name__}: {e}", exc_info=True)
        return default

def validate_input_range(value: Any, min_val: int, max_val: int) -> bool:
    """
    Validates that a value is within a specified numeric range.
    Handles non-numeric types gracefully.
    """
    try:
        if not isinstance(value, (int, float)):
            return False
        return min_val <= value <= max_val
    except Exception:
        return False

def get_nested_key(data: dict, keys: list, default: Any = None) -> Any:
    """
    Safely traverses a dictionary using a list of keys.
    """
    if not isinstance(data, dict):
        return default
    
    curr = data
    try:
        for key in keys:
            curr = curr[key]
        return curr
    except (KeyError, TypeError):
        return default