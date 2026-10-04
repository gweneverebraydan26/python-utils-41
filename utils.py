import time
import functools
import logging
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger(__name__)

def retry_network_op(exceptions: Tuple[Type[Exception], ...] = (ConnectionError, TimeoutError), 
                     tries: int = 3, 
                     delay: float = 1.0, 
                     backoff: float = 2.0):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            current_tries = tries
            current_delay = delay
            while current_tries > 0:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    current_tries -= 1
                    if current_tries == 0:
                        logger.error(f"Failed after {tries} attempts: {e}")
                        raise
                    logger.warning(f"Retrying in {current_delay}s due to: {e}")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator