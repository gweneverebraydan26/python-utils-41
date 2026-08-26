import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry(retries=3, delay=1.0, backoff=2.0, exceptions=(Exception,)):
    """Retry decorator for network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt >= retries:
                        logger.error(f"Failed {func.__name__} after {retries} attempts: {e}")
                        raise
                    logger.warning(f"Retrying {func.__name__} in {current_delay}s... (Attempt {attempt}/{retries})")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator

class NetworkClient:
    """Sample client utilizing retry logic for operations."""
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    @retry(retries=3, delay=0.5, exceptions=(ConnectionError, TimeoutError))
    def fetch_data(self) -> dict:
        """Simulate network fetch operation."""
        import random
        if random.random() < 0.7:
            raise ConnectionError("Network connection lost")
        return {"status": "success", "endpoint": self.endpoint}
