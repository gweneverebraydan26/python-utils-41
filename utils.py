import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_operation(max_attempts: int = 3, delay: float = 1.0):
    """Decorator for retrying functions on exception."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts:
                        logger.warning(f"Attempt {attempt} failed, retrying in {delay}s...")
                        time.sleep(delay)
            logger.error(f"Operation failed after {max_attempts} attempts")
            raise last_exception
        return wrapper
    return decorator

@retry_network_operation(max_attempts=3, delay=2.0)
def fetch_data(url: str):
    """Example of network-dependent function."""
    # Simulating request logic
    import random
    if random.random() < 0.7:
        raise ConnectionError("Network request failed")
    return {"status": "success"}