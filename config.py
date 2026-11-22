import json
import os
from typing import Any, Dict, Optional


class ConfigLoader:
    """Manages application configuration loading with default fallbacks."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        self._config: Dict[str, Any] = defaults.copy() if defaults else {}

    def load_from_dict(self, data: Dict[str, Any]) -> None:
        """Update configuration from a dictionary."""
        self._update_nested(self._config, data)

    def load_from_json(self, filepath: str) -> bool:
        """Load configuration settings from a JSON file."""
        if not os.path.exists(filepath):
            return False

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    self.load_from_dict(data)
                    return True
        except (json.JSONDecodeError, OSError):
            return False
        return False

    def load_from_env(self, prefix: str = "") -> None:
        """Load configuration values from environment variables."""
        for key, value in os.environ.items():
            if prefix and not key.startswith(prefix):
                continue
            config_key = key[len(prefix):].lower() if prefix else key.lower()
            self._config[config_key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value using dot notation for nested keys."""
        parts = key.split(".")
        current = self._config
        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return default
        return current

    def _update_nested(self, target: Dict[str, Any], source: Dict[str, Any]) -> None:
        """Recursively update target dictionary with source dictionary values."""
        for key, value in source.items():
            if isinstance(value, dict) and key in target and isinstance(target[key], dict):
                self._update_nested(target[key], value)
            else:
                target[key] = value

    def to_dict(self) -> Dict[str, Any]:
        """Return a copy of the current configuration as a dictionary."""
        return self._config.copy()
