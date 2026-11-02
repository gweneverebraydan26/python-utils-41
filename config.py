import json
import os
from typing import Any, Dict, Optional


class ConfigError(Exception):
    """Custom exception raised for configuration parsing and loading errors."""
    pass


class ConfigManager:
    """Manages application configuration with safe edge-case handling."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None):
        self._config: Dict[str, Any] = defaults.copy() if defaults else {}

    def load_from_file(self, filepath: str) -> bool:
        """Loads configuration from a JSON file with error boundary checks."""
        if not isinstance(filepath, str) or not filepath.strip():
            raise ConfigError("Filepath must be a non-empty string.")

        if not os.path.exists(filepath):
            raise ConfigError(f"Configuration file not found: '{filepath}'")

        try:
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                if not isinstance(data, dict):
                    raise ConfigError("Root JSON structure must be a key-value object.")
                self._config.update(data)
                return True
        except json.JSONDecodeError as err:
            raise ConfigError(f"Malformed JSON content: {err}") from err
        except (PermissionError, OSError) as err:
            raise ConfigError(f"Unable to read config file: {err}") from err

    def get(self, key_path: str, default: Any = None, target_type: Optional[type] = None) -> Any:
        """Safely retrieves a nested setting using dot notation with optional casting."""
        if not isinstance(key_path, str) or not key_path.strip():
            return default

        keys = key_path.split(".")
        current: Any = self._config

        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return default

        if target_type is not None:
            try:
                return target_type(current)
            except (ValueError, TypeError):
                return default

        return current
