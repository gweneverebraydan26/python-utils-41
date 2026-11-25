import functools
import logging
import time
from typing import Any, Callable, Tuple, Type

logger = logging.getLogger(__name__)


def retry_on_failure(
    max_retries: int = 3,
    delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    """
    Decorator that retries a function call with exponential backoff if specified exceptions occur.

    :param max_retries: Maximum number of retry attempts.
    :param delay: Initial delay between retries in seconds.
    :param backoff_factor: Multiplier applied to delay after each failed attempt.
    :param exceptions: Tuple of exception classes that trigger a retry.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    if attempt == max_retries:
                        logger.error(
                            f"Function '{func.__name__}' failed after {max_retries} attempts. Error: {exc}"
                        )
                        raise

                    logger.warning(
                        f"Attempt {attempt}/{max_retries} for '{func.__name__}' failed ({exc}). "
                        f"Retrying in {current_delay:.2f}s..."
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff_factor
        return wrapper
    return decorator
