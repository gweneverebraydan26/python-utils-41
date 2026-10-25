import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_op(retries=3, delay=1, backoff=2, exceptions=(Exception,)):
    """
    decorator for retrying network operations with exponential backoff
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == retries - 1:
                        logger.error(f"failed after {retries} attempts: {e}")
                        raise
                    
                    logger.warning(f"attempt {attempt + 1} failed, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_network_op(retries=3, delay=2)
def fetch_data(url):
    # simulate network request
    raise ConnectionError("timeout")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        fetch_data("http://example.com")
    except Exception:
        pass