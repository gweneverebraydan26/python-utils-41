import functools
import logging
import time
from typing import Callable, Any, Tuple, Type

logger = logging.getLogger(__name__)

def retry(
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
    tries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
) -> Callable:
    """
    Decorator that retries a function with exponential backoff.

    :param exceptions: A tuple of exceptions to catch and retry on.
    :param tries: The maximum number of times to try the function.
    :param delay: Initial delay between retries in seconds.
    :param backoff: Multiplier applied to delay after each retry.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt_delay = delay
            for attempt in range(1, tries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == tries:
                        logger.error(
                            f"Function '{func.__name__}' failed after {tries} attempts. Error: {e}"
                        )
                        raise
                    logger.warning(
                        f"Retrying '{func.__name__}' in {attempt_delay:.2f} seconds... (Attempt {attempt}/{tries}) due to: {e}"
                    )
                    time.sleep(attempt_delay)
                    attempt_delay *= backoff
        return wrapper
    return decorator