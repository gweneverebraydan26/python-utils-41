import functools
import time
import logging

# Configure performance logger
logger = logging.getLogger(__name__)

def memoize_with_ttl(ttl_seconds=300):
    """Decorator for caching function results with time-to-live."""
    def decorator(func):
        cache = {}

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            now = time.time()
            
            if key in cache:
                result, timestamp = cache[key]
                if now - timestamp < ttl_seconds:
                    return result
            
            result = func(*args, **kwargs)
            cache[key] = (result, now)
            return result
        return wrapper
    return decorator

@memoize_with_ttl(ttl_seconds=60)
def compute_heavy_operation(data_index: int) -> dict:
    """Simulates expensive computation with cached results."""
    # Simulate latency
    time.sleep(0.5)
    return {"index": data_index, "timestamp": time.time()}

class DataProcessor:
    """Core processor for high-frequency data handling."""
    def __init__(self, buffer_size=1024):
        self.buffer = []
        self.buffer_size = buffer_size

    def process_batch(self, items: list):
        """Batch processing optimization to reduce I/O overhead."""
        self.buffer.extend(items)
        if len(self.buffer) >= self.buffer_size:
            self._flush()

    def _flush(self):
        """Internal method to clear memory buffer."""
        logger.info(f"Flushing {len(self.buffer)} items to storage")
        self.buffer.clear()