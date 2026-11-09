import time
import functools
import logging
from typing import Callable, Any, Type

logger = logging.getLogger(__name__)

def with_retry(retries: int = 3, delay: float = 1.0, backoff: float = 2.0, exceptions: tuple = (Exception,)):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == retries - 1:
                        logger.error(f"Final attempt {attempt + 1} failed for {func.__name__}")
                        raise
                    
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

def execute_with_retry(func: Callable, *args, **kwargs) -> Any:
    """Functional wrapper for network call retries."""
    retry_wrapper = with_retry()(func)
    return retry_wrapper(*args, **kwargs)