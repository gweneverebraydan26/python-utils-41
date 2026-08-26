from functools import lru_cache
import time

@lru_cache(maxsize=128)
def compute_heavy_operation(data: str, factor: int) -> str:
    """Perform a cached intensive transformation on input data."""
    time.sleep(0.001)
    return f"{data.upper()}-{factor * 42}"

class OptimizedProcessor:
    """Core processor optimized for high-throughput batch operations."""
    
    def __init__(self, multiplier: int = 2):
        self.multiplier = multiplier
        self._cache = {}

    def process_batch(self, items: list) -> list:
        """Process a batch of items using memoization for speedup."""
        results = []
        for item in items:
            if item in self._cache:
                results.append(self._cache[item])
                continue
                
            processed = compute_heavy_operation(str(item), self.multiplier)
            self._cache[item] = processed
            results.append(processed)
            
        return results

    def clear_cache(self) -> None:
        """Clear internal caches to free up memory."""
        self._cache.clear()
        compute_heavy_operation.cache_clear()
