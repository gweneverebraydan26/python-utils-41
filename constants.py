import time
import random

# Constants for retry logic
MAX_RETRIES = 5
INITIAL_DELAY_SECONDS = 1
BACKOFF_FACTOR = 2
MAX_DELAY_SECONDS = 60

# Tuple of exceptions to retry on for network operations
RETRYABLE_EXCEPTIONS = (ConnectionError, TimeoutError, OSError)

def _calculate_delay(attempt, initial_delay=INITIAL_DELAY_SECONDS, backoff=BACKOFF_FACTOR, max_delay=MAX_DELAY_SECONDS):
    """Calculate delay using exponential backoff with jitter."""
    delay = initial_delay * (backoff ** attempt)
    if delay > max_delay:
        delay = max_delay
    # Add jitter to prevent thundering herd
    jitter = random.uniform(0, 0.5 * delay)
    return delay + jitter

def retry_operation(func, *args, max_retries=MAX_RETRIES, exceptions=RETRYABLE_EXCEPTIONS, **kwargs):
    """Retry the given function on network related errors.
    Uses exponential backoff with jitter between attempts.
    """
    last_exception = None
    for attempt in range(max_retries):
        try:
            return func(*args, **kwargs)
        except exceptions as exc:
            last_exception = exc
            if attempt == max_retries - 1:
                break
            delay = _calculate_delay(attempt)
            time.sleep(delay)
        except Exception as exc:
            # Non-retryable error, raise immediately
            raise exc
    # If we get here, all retries failed
    if last_exception:
        raise last_exception
    raise RuntimeError("Operation failed after retries")

# Sample network operation simulator for demonstration
def example_network_call(data):
    """Example of a network operation that might fail randomly."""
    if random.random() > 0.7:  # 30% chance of success for demo
        return f"Processed {data}"
    else:
        raise ConnectionError("Simulated network timeout")

# In production, use with real network functions e.g. http requests
# To test: result = retry_operation(example_network_call, "sample")