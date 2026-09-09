import functools
import re
from typing import List, Dict, Any, Generator

WHITESPACE_RE = re.compile(r'\s+')
NON_ALPHANUMERIC_RE = re.compile(r'[^a-zA-Z0-9\s]')

@functools.lru_cache(maxsize=1024)
def sanitize_string(text: str) -> str:
    """Sanitize and normalize text with memoized caching for fast repeats."""
    if not text:
        return ""
    text = NON_ALPHANUMERIC_RE.sub('', text)
    return WHITESPACE_RE.sub(' ', text).strip().lower()

def batch_process_items(items: List[Dict[str, Any]], batch_size: int = 100) -> Generator[List[Dict[str, Any]], None, None]:
    """Yield batches of dictionary items to reduce memory overhead."""
    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]

def memoized_flatten(nested_list: List[Any]) -> List[Any]:
    """Efficiently flatten a nested list using an iterative stack."""
    flat_list = []
    stack = [nested_list]
    while stack:
        current = stack.pop()
        for item in reversed(current):
            if isinstance(item, list):
                stack.append(item)
            else:
                flat_list.append(item)
    return flat_list