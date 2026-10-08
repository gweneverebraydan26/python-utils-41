import collections.abc
from itertools import islice
from typing import Iterable, Iterator, Any, Generator

def chunked(iterable: Iterable[Any], size: int) -> Generator[list[Any], None, None]:
    """Break an iterable into lists of a given size without loading everything."""
    if size < 1:
        raise ValueError("Chunk size must be at least 1")
    iterator = iter(iterable)
    while True:
        chunk = list(islice(iterator, size))
        if not chunk:
            break
        yield chunk

def fast_flatten(iterable: Iterable[Any]) -> Generator[Any, None, None]:
    """Flatten deeply nested iterables iteratively to optimize memory and speed.

    Avoids recursion limits by using an internal stack.
    """
    stack = [iter(iterable)]
    while stack:
        try:
            item = next(stack[-1])
            if isinstance(item, (str, bytes)):
                yield item
            elif isinstance(item, collections.abc.Iterable):
                stack.append(iter(item))
            else:
                yield item
        except StopIteration:
            stack.pop()
