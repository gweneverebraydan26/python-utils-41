import os
import json
from typing import Any, Dict, Optional, Type, TypeVar

T = TypeVar('T')

class ConfigError(Exception):
    """Custom exception raised for configuration validation errors."""
    pass

class SafeConfig:
    """A utility to safely extract and cast configuration values from env or dict."""

    def __init__(self, data: Optional[Dict[str, Any]] = None):
        self._data = data or {}

    def get_as_type(self, key: str, expected_type: Type[T], default: Optional[T] = None) -> T:
        """
        Retrieve a config value and cast it to the expected type.
        Handles edge cases like boolean strings, malformed JSON, and numeric casting.
        """
        value = self._data.get(key)

        if value is None:
            value = os.environ.get(key)

        if value is None:
            if default is not None:
                return default
            raise ConfigError(f"Missing required configuration key: '{key}'")

        if expected_type is bool:
            if isinstance(value, str):
                normalized = value.strip().lower()
                if normalized in ('true', '1', 'yes', 'on'):
                    return True  # type: ignore
                if normalized in ('false', '0', 'no', 'off'):
                    return False  # type: ignore
                raise ConfigError(f"Cannot cast value '{value}' for key '{key}' to boolean")
            return bool(value)  # type: ignore

        try:
            if expected_type in (int, float):
                return expected_type(value)  # type: ignore

            if expected_type in (list, dict) and isinstance(value, str):
                try:
                    parsed = json.loads(value)
                    if isinstance(parsed, expected_type):
                        return parsed
                except json.JSONDecodeError as err:
                    raise ConfigError(f"Failed to parse JSON structure for key '{key}': {err}") from err

            if not isinstance(value, expected_type):
                return expected_type(value)  # type: ignore

            return value
        except (ValueError, TypeError) as err:
            raise ConfigError(
                f"Type conversion failed for key '{key}'. "
                f"Expected {expected_type.__name__}, got value '{value}'"
            ) from err