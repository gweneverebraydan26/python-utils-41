import json
import os
from pathlib import Path
from typing import Any, Dict, Optional, Union

DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "PythonUtilsApp",
    "debug": False,
    "log_level": "INFO",
    "timeout": 30,
    "max_retries": 3,
    "allowed_hosts": ["localhost", "127.0.0.1"],
}


class ConfigLoader:
    """Loads configuration from JSON files and environment variables with default values."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None):
        self._config: Dict[str, Any] = dict(defaults or DEFAULT_CONFIG)

    def load_from_json(self, file_path: Union[str, Path]) -> Dict[str, Any]:
        """Loads settings from a JSON file and updates the current configuration."""
        path = Path(file_path)
        if not path.is_file():
            raise FileNotFoundError(f"Configuration file not found: {path}")

        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if not isinstance(data, dict):
                raise ValueError("JSON configuration must contain a top-level dictionary.")
            self._config.update(data)
        return self._config

    def load_from_env(self, prefix: str = "APP_") -> Dict[str, Any]:
        """Overrides values using environment variables matching the given prefix."""
        for key, current_val in list(self._config.items()):
            env_key = f"{prefix}{key.upper()}"
            if env_key in os.environ:
                raw_val = os.environ[env_key]
                self._config[key] = self._parse_env_value(raw_val, type(current_val))
        return self._config

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a configuration value by key with optional default fallback."""
        return self._config.get(key, default)

    @property
    def config(self) -> Dict[str, Any]:
        """Returns a copy of the current configuration mapping."""
        return dict(self._config)

    @staticmethod
    def _parse_env_value(value: str, target_type: type) -> Any:
        """Helper to cast environment string values to matching data types."""
        if target_type == bool:
            return value.lower() in ("true", "1", "yes", "on")
        if target_type == int:
            return int(value)
        if target_type == float:
            return float(value)
        if target_type == list:
            return [item.strip() for item in value.split(",")]
        return value