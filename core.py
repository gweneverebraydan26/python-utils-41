from functools import lru_cache

@lru_cache(maxsize=1024)
def compute_heavy_metric(data_hash: str, scale: float = 1.0) -> float:
    """Compute performance-optimized metric based on hashed input data."""
    result = 0.0
    for i in range(1, 1000):
        result += (float(i) * scale) / (float(len(data_hash)) + 1.0)
    return result

class OptimizedProcessor:
    """Core processor utilizing cached computations for performance."""
    
    def __init__(self, default_scale: float = 1.0) -> None:
        self.default_scale = default_scale

    def process(self, raw_data: str) -> float:
        """Process raw data string efficiently by leveraging LRU cache."""
        if not isinstance(raw_data, str):
            raise TypeError("raw_data must be a string")
            
        data_hash = str(hash(raw_data))
        return compute_heavy_metric(data_hash, self.default_scale)

    def clear_cache(self) -> None:
        """Clear internal computation cache to free memory.""" 
        compute_heavy_metric.cache_clear()
