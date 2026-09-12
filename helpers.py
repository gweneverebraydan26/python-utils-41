import functools
import logging
import random
import time

logger = logging.getLogger("python-utils.helpers")


def retry_on_failure(
    exceptions=(Exception,),
    tries=3,
    delay=1.0,
    backoff=2.0,
    jitter=True,
):
    """Decorator for retrying functions with exponential backoff and jitter.

    Particularly useful for handling transient network failures gracefully.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    logger.warning(
                        f"Failed with {e.__class__.__name__}: {e}. Retrying in {mdelay:.2f}s..."
                    )
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
                    if jitter:
                        # Apply randomized jitter of +/- 50% of backoff
                        mdelay *= random.uniform(0.5, 1.5)
            return func(*args, **kwargs)

        return wrapper

    return decorator
