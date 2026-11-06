import time
import random
import logging
from typing import Callable, Type, Tuple, Any

logger = logging.getLogger(__name__)


def retry_network_op(
    retries: int = 3,
    backoff_factor: float = 0.5,
    exceptions: Tuple[Type[Exception], ...] = (Exception,),
    jitter: bool = True
) -> Callable:
    """
    Decorator that retries a function upon specified exceptions with exponential backoff.
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    attempt += 1
                    if attempt >= retries:
                        logger.error(
                            f"Operation '{func.__name__}' failed after {retries} attempts: {err}"
                        )
                        raise
                    
                    delay = backoff_factor * (2 ** (attempt - 1))
                    if jitter:
                        delay += random.uniform(0, 0.1 * delay)
                    
                    logger.warning(
                        f"Attempt {attempt}/{retries} for '{func.__name__}' failed: {err}. Retrying in {delay:.2f}s..."
                    )
                    time.sleep(delay)
        return wrapper
    return decorator


def execute_with_retry(
    func: Callable,
    *args: Any,
    retries: int = 3,
    backoff_factor: float = 0.5,
    exceptions: Tuple[Type[Exception], ...] = (Exception,),
    **kwargs: Any
) -> Any:
    """
    Executes a callable with configurable retry logic and backoff delay.
    """
    retry_decorator = retry_network_op(
        retries=retries,
        backoff_factor=backoff_factor,
        exceptions=exceptions
    )
    return retry_decorator(func)(*args, **kwargs)
