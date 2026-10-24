import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

def safe_execute(func: callable, *args: Any, **kwargs: Any) -> Optional[Any]:
    """Executes a function safely with error handling for edge cases."""
    try:
        return func(*args, **kwargs)
    except (ValueError, TypeError) as e:
        logger.error(f"Invalid input provided: {e}")
        return None
    except ZeroDivisionError:
        logger.error("Arithmetic error: division by zero")
        return None
    except Exception as e:
        logger.critical(f"Unexpected system failure: {e}")
        raise

def parse_int_safe(value: Any, default: int = 0) -> int:
    """Converts input to integer with fallback for invalid types."""
    try:
        return int(value)
    except (ValueError, TypeError, OverflowError):
        return default

def validate_connection_string(conn_str: Optional[str]) -> bool:
    """Validates string input for null or empty edge cases."""
    if conn_str is None:
        return False
    if not isinstance(conn_str, str):
        return False
    return len(conn_str.strip()) > 0