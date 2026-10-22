import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry(exceptions, tries=3, delay=1, backoff=2):
    """
    Decorator for retrying network operations with exponential backoff.
    
    :param exceptions: Tuple of exception classes to catch.
    :param tries: Maximum number of attempts.
    :param delay: Initial delay between retries in seconds.
    :param backoff: Multiplier for delay after each retry.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    logger.warning(f"{func.__name__} failed: {e}, retrying in {mdelay}s...")
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator