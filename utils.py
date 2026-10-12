import functools
import logging
import random
import time
from typing import Any, Callable, Tuple, Type, Union

logger = logging.getLogger(__name__)


def retry(
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    jitter: bool = True,
    exceptions: Union[Type[BaseException], Tuple[Type[BaseException], ...]] = Exception,
) -> Callable:
    """Decorator to retry network operations with exponential backoff and jitter."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    if attempt == retries:
                        logger.error("Execution '%s' failed after %d retries: %s", func.__name__, retries, exc)
                        raise exc

                    sleep_time = current_delay + (random.uniform(0, current_delay * 0.1) if jitter else 0)
                    logger.warning(
                        "Attempt %d/%d for '%s' failed: %s. Retrying in %.2fs...",
                        attempt, retries, func.__name__, exc, sleep_time
                    )
                    time.sleep(sleep_time)
                    current_delay *= backoff

        return wrapper
    return decorator
