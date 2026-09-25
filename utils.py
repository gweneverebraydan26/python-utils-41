import time
import random
import functools
from typing import Callable, Any, Type, Tuple


def retry(
    retries: int = 3,
    backoff_factor: float = 0.5,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
    jitter: bool = True,
) -> Callable:
    """
    Decorator that retries a function if specified exceptions are raised.

    Uses exponential backoff with optional random jitter.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    attempts += 1
                    if attempts > retries:
                        raise err
                    
                    delay = backoff_factor * (2 ** (attempts - 1))
                    if jitter:
                        delay += random.uniform(0, delay * 0.1)
                    
                    time.sleep(delay)

        return wrapper
    return decorator


def retry_call(
    func: Callable,
    args: Tuple[Any, ...] = (),
    kwargs: dict = None,
    retries: int = 3,
    backoff_factor: float = 0.5,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
) -> Any:
    """
    Executes a callable with retry logic and exponential backoff.
    """
    if kwargs is None:
        kwargs = {}
    
    decorated = retry(
        retries=retries,
        backoff_factor=backoff_factor,
        exceptions=exceptions,
    )(func)
    return decorated(*args, **kwargs)
