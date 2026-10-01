import json
import os
from pathlib import Path
from typing import Any, Dict, Union

DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "PythonUtilsApp",
    "version": "1.0.0",
    "debug": False,
    "log_level": "INFO",
    "max_retries": 3,
    "timeout": 30,
}


class ConfigManager:
    """Manages application configuration with default fallback support."""

    def __init__(self, defaults: Dict[str, Any] = None):
        self._config: Dict[str, Any] = dict(defaults or DEFAULT_CONFIG)

    def load_from_json(self, filepath: Union[str, Path]) -> None:
        """Load settings from a JSON file and merge with existing defaults."""
        path = Path(filepath)
        if path.is_file():
            with path.open("r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    self.update(data)

    def load_from_env(self, prefix: str = "APP_") -> None:
        """Load settings from environment variables matching prefix."""
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix) :].lower()
                self._config[config_key] = self._parse_env_value(value)

    def update(self, updates: Dict[str, Any]) -> None:
        """Update configuration dictionary values."""
        self._config.update(updates)

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key."""
        return self._config.get(key, default)

    def _parse_env_value(self, val: str) -> Any:
        """Convert string environment variables to appropriate primitive types."""
        if val.lower() in ("true", "1", "yes"):
            return True
        if val.lower() in ("false", "0", "no"):
            return False
        try:
            return int(val)
        except ValueError:
            try:
                return float(val)
            except ValueError:
                return val

    def to_dict(self) -> Dict[str, Any]:
        """Return full configuration dictionary copy."""
        return self._config.copy()
