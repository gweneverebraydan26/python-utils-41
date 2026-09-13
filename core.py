import time
from typing import Any, Dict, Generator, Iterable, List
from contextlib import contextmanager

def chunk_iterable(iterable: Iterable[Any], size: int) -> Generator[List[Any], None, None]:
    """Yield successive n-sized chunks from an iterable."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk

def safe_get(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    """Retrieve a nested value from a dictionary using a dot-separated path."""
    keys = path.split(".")
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

@contextmanager
def execution_timer() -> Generator[Dict[str, float], None, None]:
    """Context manager to measure the execution time of a code block."""
    stats = {"start": time.perf_counter(), "elapsed": 0.0}
    try:
        yield stats
    finally:
        stats["elapsed"] = time.perf_counter() - stats["start"]
