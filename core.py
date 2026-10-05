import threading
from typing import Any, Callable, Generator, Iterable, List, TypeVar

T = TypeVar("T")

class lazy_property:
    """A performance-optimized, thread-safe descriptor that caches a property.
    
    Subsequent accesses avoid re-evaluation overhead entirely.
    """
    def __init__(self, fget: Callable[[Any], Any]) -> None:
        self.fget = fget
        self.__doc__ = fget.__doc__
        self.__name__ = fget.__name__
        self._lock = threading.RLock()

    def __get__(self, obj: Any, cls: Any) -> Any:
        if obj is None:
            return self
        
        obj_dict = obj.__dict__
        name = self.__name__
        if name in obj_dict:
            return obj_dict[name]

        with self._lock:
            # Double-check lock pattern to handle race conditions safely
            if name not in obj_dict:
                obj_dict[name] = self.fget(obj)
            return obj_dict[name]


def chunk_iterable(iterable: Iterable[T], size: int) -> Generator[List[T], None, None]:
    """Yields successive chunks from an iterable in a memory-efficient manner.
    
    Optimized to minimize object allocation and generator overhead.
    """
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero.")

    iterator = iter(iterable)
    while True:
        chunk = []
        for _ in range(size):
            try:
                chunk.append(next(iterator))
            except StopIteration:
                break
        if not chunk:
            break
        yield chunk


def deep_merge(dict1: dict, dict2: dict) -> dict:
    """Performance-optimized, iterative deep merge of two dictionaries.
    
    Bypasses recursion depth limits and overhead by using a stack.
    """
    destination = dict1.copy()
    stack = [(destination, dict2)]

    while stack:
        target, source = stack.pop()
        for key, value in source.items():
            if key in target:
                target_val = target[key]
                if isinstance(target_val, dict) and isinstance(value, dict):
                    target[key] = target_val.copy()
                    stack.append((target[key], value))
                else:
                    target[key] = value
            else:
                target[key] = value
    return destination