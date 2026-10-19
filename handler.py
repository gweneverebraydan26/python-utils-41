import logging
from typing import Any, Callable, Optional

logger = logging.getLogger(__name__)

def safe_execute(func: Callable, *args: Any, **kwargs: Any) -> Optional[Any]:
    """
    Executes a function with standardized error handling
    for common edge cases and unexpected failures.
    """
    try:
        return func(*args, **kwargs)
    except TypeError as e:
        logger.error(f"Invalid arguments provided to {func.__name__}: {e}")
    except ValueError as e:
        logger.error(f"Value error in {func.__name__}: {e}")
    except AttributeError as e:
        logger.error(f"Attribute missing in {func.__name__}: {e}")
    except Exception as e:
        logger.critical(f"Unexpected error during {func.__name__}: {e}", exc_info=True)
    return None

def validate_input(data: Any, expected_type: type) -> bool:
    """
    Validates data against a type to prevent processing errors.
    """
    if data is None:
        logger.warning("Received null input for validation")
        return False
    if not isinstance(data, expected_type):
        logger.warning(f"Expected {expected_type}, got {type(data)}")
        return False
    return True