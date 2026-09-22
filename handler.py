import logging
from typing import Any, Callable, Optional

logger = logging.getLogger(__name__)

class OperationHandler:
    """Utility class for robust function execution."""

    @staticmethod
    def safe_execute(func: Callable, *args: Any, default: Any = None, **kwargs: Any) -> Any:
        """Executes a function and returns default value on failure."""
        try:
            return func(*args, **kwargs)
        except (ValueError, TypeError, KeyError, IndexError) as e:
            logger.error(f"Data processing error in {func.__name__}: {e}")
            return default
        except Exception as e:
            logger.critical(f"Unexpected system failure in {func.__name__}: {e}", exc_info=True)
            raise

    def validate_input(self, value: Any, expected_type: type) -> bool:
        """Validates input types to prevent runtime crashes."""
        if value is None:
            return False
        if not isinstance(value, expected_type):
            logger.warning(f"Type mismatch: expected {expected_type}, got {type(value)}")
            return False
        return True

    def process_with_retry(self, func: Callable, retries: int = 3) -> Optional[Any]:
        """Executes logic with basic retry mechanism for intermittent issues."""
        for attempt in range(retries):
            try:
                return func()
            except Exception as e:
                if attempt == retries - 1:
                    logger.error(f"Final attempt failed for {func.__name__}")
                    return None
                continue
        return None