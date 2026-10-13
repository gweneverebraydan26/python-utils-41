import time
import functools
import random
from typing import Callable, Any

def with_retry(max_attempts: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            last_exception = None
            
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        time.sleep(current_delay)
                        current_delay *= backoff
            
            raise last_exception
        return wrapper
    return decorator

@with_retry(max_attempts=3, delay=2.0)
def fetch_remote_data(url: str):
    """Simulates a network request that may fail."""
    # Example implementation context
    if random.random() < 0.7:
        raise ConnectionError("Failed to reach server")
    return {"status": "success", "data": "sample"}