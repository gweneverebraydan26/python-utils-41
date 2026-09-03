import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry(exceptions, tries=3, delay=1.0, backoff=2.0):
    """
    Decorator to retry a function call with exponential backoff.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    logger.warning(f'{e}. Retrying in {mdelay} seconds...')
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator