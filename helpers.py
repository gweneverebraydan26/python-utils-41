import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry(max_attempts=3, delay=1, backoff=2, exceptions=(Exception,)):
    """Decorator to retry network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_attempts:
                        logger.error(f"Final attempt {attempt} failed for {func.__name__}")
                        raise e
                    
                    logger.warning(f"Attempt {attempt} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2)
def network_request_stub(url):
    """Example network operation function."""
    # Simulating volatile network conditions
    import random
    if random.random() < 0.7:
        raise ConnectionError("Transient network error")
    return f"Success fetching {url}"