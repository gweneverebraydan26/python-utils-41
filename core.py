import logging
from typing import Any, Optional, Callable

logger = logging.getLogger(__name__)

def safe_execute(func: Callable, *args: Any, default: Any = None, **kwargs: Any) -> Any:
    """Execute a callable with broad exception handling and logging."""
    try:
        return func(*args, **kwargs)
    except (ValueError, TypeError, AttributeError) as e:
        logger.error(f"Execution error in {func.__name__}: {str(e)}")
        return default
    except Exception as e:
        logger.critical(f"Unexpected system failure: {str(e)}", exc_info=True)
        raise

def validate_payload(data: Any, schema_keys: list) -> bool:
    """Check dictionary keys against schema with graceful failure."""
    if not isinstance(data, dict):
        logger.warning("Invalid input type: expected dictionary")
        return False
    
    try:
        return all(key in data for key in schema_keys)
    except TypeError:
        return False

def get_nested(data: dict, path: str, default: Any = None) -> Any:
    """Access nested keys safely using dot notation."""
    keys = path.split('.')
    current = data
    try:
        for key in keys:
            if isinstance(current, dict):
                current = current.get(key)
            else:
                return default
        return current if current is not None else default
    except (AttributeError, KeyError):
        return default