import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Manages application configuration with defaults and environmental overrides."""

    def __init__(self, defaults: Dict[str, Any]):
        self._defaults = defaults
        self._config = defaults.copy()

    def load_from_dict(self, data: Dict[str, Any]) -> None:
        """Merges configuration updates from a dictionary."""
        for key, value in data.items():
            if isinstance(value, dict) and isinstance(self._config.get(key), dict):
                self._config[key] = {**self._config[key], **value}
            else:
                self._config[key] = value

    def load_from_json(self, filepath: str) -> bool:
        """Loads configuration from a JSON file if it exists."""
        if not os.path.exists(filepath):
            return False
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.load_from_dict(data)
        return True

    def load_from_env(self, prefix: str = "APP_") -> None:
        """Overrides existing configuration using matching environment variables."""
        for key in list(self._config.keys()):
            env_key = f"{prefix}{key.upper()}"
            if env_key in os.environ:
                raw_val = os.environ[env_key]
                try:
                    # Try parsing env value as JSON (handles bools, numbers, lists)
                    self._config[key] = json.loads(raw_val)
                except json.JSONDecodeError:
                    self._config[key] = raw_val

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a configuration value by key."""
        return self._config.get(key, default)

    @property
    def data(self) -> Dict[str, Any]:
        """Returns the resolved configuration dictionary."""
        return self._config