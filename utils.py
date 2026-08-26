import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry(retries=3, delay=2, backoff=2, exceptions=(Exception,)):
    """Retry decorator with exponential backoff for network operations."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            mt_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == retries:
                        logger.error(f"Failed after {retries} attempts: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt} failed: {e}. Retrying in {mt_delay}s...")
                    time.sleep(mt_delay)
                    mt_delay *= backoff
        return wrapper
    return decorator
