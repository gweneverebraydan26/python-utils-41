import functools
import logging
import time
from typing import Any, Callable, Tuple, Type, TypeVar

logger = logging.getLogger(__name__)

F = TypeVar("F", bound=Callable[..., Any])


def retry_network_call(
    max_retries: int = 3,
    delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: Tuple[Type[BaseException], ...] = (ConnectionError, TimeoutError, OSError),
) -> Callable[[F], F]:
    """Decorator that retries network functions using exponential backoff.

    Args:
        max_retries: Maximum number of retry attempts.
        delay: Initial delay between retries in seconds.
        backoff_factor: Multiplier applied to delay after each failure.
        exceptions: Tuple of exception classes that trigger a retry.
    """

    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            last_exception = None

            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    last_exception = exc
                    if attempt == max_retries:
                        logger.error(
                            f"Operation '{func.__name__}' failed after {max_retries} attempts."
                        )
                        raise

                    logger.warning(
                        f"Attempt {attempt}/{max_retries} for '{func.__name__}' failed: {exc}. "
                        f"Retrying in {current_delay:.2f}s..."
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff_factor

            if last_exception:
                raise last_exception

        return wrapper  # type: ignore

    return decorator
