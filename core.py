import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry(max_attempts: int = 3, delay: float = 1.0, exceptions: tuple = (Exception,)): 
    """Decorator for retrying network operations with backoff."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        logger.error(f"Failed after {max_attempts} attempts: {e}")
                        raise
                    time.sleep(delay * attempts)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2.0)
def fetch_url(url: str) -> str:
    """Example network operation function."""
    # Simulates potential transient network failure
    import random
    if random.random() < 0.5:
        raise ConnectionError("Transient network error occurred")
    return f"Content from {url}"