import logging
from typing import Any, Callable, Optional

logger = logging.getLogger(__name__)

def safe_execute(func: Callable, *args: Any, **kwargs: Any) -> Optional[Any]:
    """Executes a callable with robust error handling for edge cases."""
    try:
        return func(*args, **kwargs)
    except TypeError as e:
        logger.error(f"Type mismatch in {func.__name__}: {e}")
    except ValueError as e:
        logger.error(f"Invalid value provided to {func.__name__}: {e}")
    except KeyError as e:
        logger.error(f"Missing required key in {func.__name__}: {e}")
    except AttributeError as e:
        logger.error(f"Object missing expected attribute in {func.__name__}: {e}")
    except Exception as e:
        logger.critical(f"Unexpected system error in {func.__name__}: {e}", exc_info=True)
    return None

def validate_input(data: Any, expected_type: type) -> bool:
    """Checks if data exists and matches expected type."""
    try:
        if data is None:
            return False
        if not isinstance(data, expected_type):
            return False
        return True
    except Exception:
        return False