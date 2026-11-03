import functools
from typing import Any, List, Tuple


class FastTaskRunner:
    """Core task runner optimized with caching and execution batching."""

    def __init__(self, cache_size: int = 128) -> None:
        self.cache_size = cache_size
        # Decorate internal execution function with LRU cache for fast repeated lookups
        self._memoized_exec = functools.lru_cache(maxsize=cache_size)(
            self._compute_task
        )

    @staticmethod
    def _compute_task(task_name: str, payload_hash: int, data: str) -> str:
        """Internal compute method that performs CPU-bound string transformations."""
        reversed_str = data[::-1]
        return f"{task_name}:{payload_hash}:{reversed_str}"

    def run(self, task_name: str, data: str) -> str:
        """Execute a task using the cached internal compute method."""
        payload_hash = hash(data)
        return self._memoized_exec(task_name, payload_hash, data)

    def batch_run(self, tasks: List[Tuple[str, str]]) -> List[str]:
        """Process multiple task payloads sequentially using cached lookups."""
        return [self.run(task_name, data) for task_name, data in tasks]

    def cache_info(self) -> Any:
        """Return current cache statistics for monitoring optimization efficiency."""
        return self._memoized_exec.cache_info()

    def clear_cache(self) -> None:
        """Clear cached computation results to free memory."""
        self._memoized_exec.cache_clear()
