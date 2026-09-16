import time
import functools
import logging
from typing import Callable, Any, Type

logger = logging.getLogger(__name__)

def retry_on_network_failure(retries: int = 3, delay: float = 1.0, exceptions: tuple = (ConnectionError, TimeoutError)) -> Callable:
    """Decorator to retry network-related functions with exponential backoff."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            attempt = 0
            current_delay = delay
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt == retries:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt} failed for {func.__name__}, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= 2
        return wrapper
    return decorator