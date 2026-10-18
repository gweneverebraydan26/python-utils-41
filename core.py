import random
import time
from functools import wraps
from typing import Callable, Any, Tuple, Type


def retry_network_op(
    max_retries: int = 3,
    backoff_factor: float = 1.0,
    exceptions: Tuple[Type[BaseException], ...] = (ConnectionError, TimeoutError, OSError),
    jitter: bool = True,
) -> Callable:
    """Decorator that retries a network operation with exponential backoff.

    Args:
        max_retries: Maximum number of retry attempts allowed.
        backoff_factor: Multiplier for exponential delay calculation.
        exceptions: Tuple of exception types to catch and trigger retries.
        jitter: Adds random noise to delay calculation to avoid thundering herd.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    attempts += 1
                    if attempts > max_retries:
                        raise exc

                    # Calculate exponential backoff delay
                    delay = backoff_factor * (2 ** (attempts - 1))
                    if jitter:
                        delay += random.uniform(0, 0.5 * delay)

                    time.sleep(delay)
        return wrapper
    return decorator


class NetworkRetrier:
    """Context manager or runner for executing network calls with retry policies."""

    def __init__(
        self, 
        max_retries: int = 3, 
        delay: float = 1.0, 
        exceptions: Tuple[Type[BaseException], ...] = (ConnectionError, TimeoutError)
    ):
        self.max_retries = max_retries
        self.delay = delay
        self.exceptions = exceptions

    def execute(self, func: Callable, *args: Any, **kwargs: Any) -> Any:
        """Executes a target function applying the configured retry limits."""
        for attempt in range(1, self.max_retries + 2):
            try:
                return func(*args, **kwargs)
            except self.exceptions as exc:
                if attempt > self.max_retries:
                    raise exc
                time.sleep(self.delay * (2 ** (attempt - 1)))
