import functools
import random
import time
from typing import Any, Callable, Tuple, Type, TypeVar

T = TypeVar("T")


def retry_network_op(
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    jitter: bool = True,
    retryable_exceptions: Tuple[Type[Exception], ...] = (Exception,),
) -> Callable:
    """Decorator that retries network or fragile operations with exponential backoff.

    Args:
        max_retries: Maximum number of attempts before raising the exception.
        initial_delay: Initial waiting time in seconds between retries.
        backoff_factor: Multiplier applied to delay after each failed attempt.
        jitter: Adds randomness to delay to prevent thundering herd issues.
        retryable_exceptions: Tuple of exception classes to intercept and retry.
    """
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            delay = initial_delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except retryable_exceptions as exc:
                    if attempt == max_retries:
                        raise exc
                    
                    sleep_time = delay * (1 + random.random()) if jitter else delay
                    time.sleep(sleep_time)
                    delay *= backoff_factor
            
            raise RuntimeError("Retry limit reached without catching exception")
            
        return wrapper
    return decorator
