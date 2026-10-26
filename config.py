import json
import os
from typing import Any, Dict, Optional


class ConfigLoader:
    """Manages application configuration with default fallback values."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None):
        self._config: Dict[str, Any] = defaults.copy() if defaults else {}

    def load_from_dict(self, data: Dict[str, Any]) -> None:
        """Update configuration settings from a dictionary."""
        self._config.update(data)

    def load_from_json(self, filepath: str) -> bool:
        """Load configuration from a JSON file if it exists."""
        if not os.path.exists(filepath):
            return False

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    self.load_from_dict(data)
                    return True
        except (json.JSONDecodeError, OSError):
            pass
        return False

    def load_from_env(self, prefix: str = "APP_") -> None:
        """Override configuration options using environment variables."""
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix) :].lower()
                try:
                    self._config[config_key] = json.loads(value)
                except (json.JSONDecodeError, TypeError):
                    self._config[config_key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value with optional default fallback."""
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set a configuration value dynamically."""
        self._config[key] = value

    def to_dict(self) -> Dict[str, Any]:
        """Return a copy of the active configuration dictionary."""
        return self._config.copy()
