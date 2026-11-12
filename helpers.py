import time
import functools
import logging
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger(__name__)

def retry_on_failure(exceptions: Tuple[Type[Exception], ...] = (Exception,), 
                     max_retries: int = 3, 
                     delay: float = 1.0):
    """Decorator to retry network functions on failure."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            
            logger.error(f"Final attempt failed after {max_retries} retries.")
            raise last_exception
        return wrapper
    return decorator