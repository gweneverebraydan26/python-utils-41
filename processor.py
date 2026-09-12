import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_operation(max_retries=3, delay=1.0, backoff=2.0, exceptions=(Exception,)):
    """Decorator to retry network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            last_exception = None

            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt == max_retries:
                        break
                    
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            
            logger.error(f"Operation failed after {max_retries} retries.")
            raise last_exception
        return wrapper
    return decorator

@retry_operation(max_retries=3, delay=2.0)
def fetch_network_data(url):
    """Example function performing network I/O."""
    # Simulating actual network logic
    import random
    if random.random() < 0.7:
        raise ConnectionError("Temporary server timeout")
    return {"status": "success", "url": url}