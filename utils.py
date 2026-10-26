import time
import functools
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def retry_network_operation(max_retries=3, delay=1.0, backoff=2.0):
    """Decorator for retrying functions on exception."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= max_retries:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempts} failed for {func.__name__}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

@retry_network_operation(max_retries=3, delay=2.0)
def fetch_data(url):
    """Example function performing a simulated network call."""
    # Placeholder for actual request logic like requests.get
    logger.info(f"Fetching data from {url}")
    raise ConnectionError("Service unavailable")