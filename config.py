import json
import os
from typing import Any, Dict, Optional


class ConfigLoader:
    """Utility class to load configuration options with default fallbacks."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        self._defaults: Dict[str, Any] = defaults.copy() if defaults else {}
        self._config: Dict[str, Any] = self._defaults.copy()

    def load_from_dict(self, data: Dict[str, Any]) -> None:
        """Merge configuration settings from a dictionary."""
        if not isinstance(data, dict):
            raise TypeError("Configuration data must be a dictionary")
        self._config.update(data)

    def load_from_json(self, filepath: str) -> None:
        """Load configuration settings from a JSON file."""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Configuration file not found: {filepath}")

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, dict):
            raise ValueError("JSON configuration must contain a root object")

        self.load_from_dict(data)

    def load_from_env(self, prefix: str = "") -> None:
        """Load configuration options from environment variables."""
        for key, value in os.environ.items():
            if prefix and not key.startswith(prefix):
                continue
            config_key = key[len(prefix):].lower() if prefix else key.lower()
            if config_key:
                try:
                    self._config[config_key] = json.loads(value)
                except (json.JSONDecodeError, TypeError):
                    self._config[config_key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key."""
        return self._config.get(key, default)

    def to_dict(self) -> Dict[str, Any]:
        """Return the complete merged configuration as a dictionary."""
        return self._config.copy()
