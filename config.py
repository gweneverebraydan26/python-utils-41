import functools
import logging
from typing import Any, Callable

# global registry for cached configuration values
_CONFIG_CACHE = {}

class ConfigManager:
    """Thread-safe configuration accessor with memoization."""

    def __init__(self) -> None:
        self._settings = {}

    @functools.lru_cache(maxsize=128)
    def get_setting(self, key: str, default: Any = None) -> Any:
        """retrieve setting value with lru_cache performance boost."""
        return self._settings.get(key, default)

    def update_setting(self, key: str, value: Any) -> None:
        """update setting and clear specific cache entries."""
        self._settings[key] = value
        self.get_setting.cache_clear()

    def bulk_load(self, data: dict) -> None:
        """bulk update for dictionary configurations."""
        self._settings.update(data)
        self.get_setting.cache_clear()

def memoized_config(func: Callable) -> Callable:
    """decorator for expensive configuration lookup methods."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (func.__name__, str(args), str(kwargs))
        if key not in _CONFIG_CACHE:
            _CONFIG_CACHE[key] = func(*args, **kwargs)
        return _CONFIG_CACHE[key]
    return wrapper