import os
from typing import Any, Callable, TypeVar

T = TypeVar("T")


class ConfigManager:
    """A configuration utility to retrieve and cast environment variables safely."""

    def __init__(self, prefix: str = "") -> None:
        """Initialize the manager with an optional environment variable prefix.

        Args:
            prefix: A prefix to prepended to all environment variable lookups.
        """
        self.prefix = prefix

    def _build_key(self, key: str) -> str:
        """Construct the full environment variable key name."""
        return f"{self.prefix}{key}" if self.prefix else key

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve an environment variable value as a string.

        Args:
            key: The configuration option name.
            default: The fallback value if the environment variable is not set.
        """
        full_key = self._build_key(key)
        return os.environ.get(full_key, default)

    def get_as(self, key: str, cast_type: Callable[[str], T], default: T) -> T:
        """Retrieve an environment variable and safely cast it to a target type.

        Args:
            key: The configuration option name.
            cast_type: A callable used to cast the string value (e.g., int, float).
            default: The fallback value if configuration is missing or casting fails.
        """
        val = self.get(key)
        if val is None:
            return default
        
        try:
            if cast_type is bool:
                return str(val).lower() in ("true", "1", "t", "y", "yes")  # type: ignore
            return cast_type(val)
        except (ValueError, TypeError):
            return default
