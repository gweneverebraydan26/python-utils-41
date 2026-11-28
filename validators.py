import functools
import re
from typing import Any, Callable

# Compiled regex cache for performance
_REGEX_CACHE = {}

def memoized_validator(func: Callable) -> Callable:
    """Cache validator results to improve performance."""
    @functools.lru_cache(maxsize=128)
    def wrapper(value: Any) -> bool:
        return func(value)
    return wrapper

@memoized_validator
def is_alphanumeric(value: str) -> bool:
    """Validate alphanumeric strings efficiently."""
    if not isinstance(value, str):
        return False
    return value.isalnum()

def validate_pattern(value: str, pattern: str) -> bool:
    """Match strings against compiled regex patterns."""
    if pattern not in _REGEX_CACHE:
        _REGEX_CACHE[pattern] = re.compile(pattern)
    return bool(_REGEX_CACHE[pattern].match(value))

def batch_validate(items: list, validator: Callable) -> list:
    """Execute validation over collection using list comprehension."""
    return [item for item in items if validator(item)]