import json
from pathlib import Path
from typing import Any, Dict, Optional, Union


class ConfigLoader:
    """Manages application configuration with default values and JSON file overrides."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None):
        self._defaults = defaults or {}
        self._config = self._deep_copy(self._defaults)

    def _deep_copy(self, data: Dict[str, Any]) -> Dict[str, Any]:
        return json.loads(json.dumps(data))

    def _merge_dicts(self, base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
        """Recursively merge override dictionary into base dictionary."""
        merged = self._deep_copy(base)
        for key, value in override.items():
            if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
                merged[key] = self._merge_dicts(merged[key], value)
            else:
                merged[key] = value
        return merged

    def load_from_dict(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Merge custom configuration dictionary over existing config."""
        self._config = self._merge_dicts(self._config, data)
        return self._config

    def load_from_file(self, filepath: Union[str, Path]) -> Dict[str, Any]:
        """Load configuration from a JSON file and merge with current values."""
        path = Path(filepath)
        if not path.exists():
            raise FileNotFoundError(f"Config file not found: {filepath}")

        with open(path, "r", encoding="utf-8") as f:
            file_data = json.load(f)

        return self.load_from_dict(file_data)

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve configuration value using dot notation for nested keys."""
        parts = key.split(".")
        current = self._config
        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return default
        return current

    def reset(self) -> None:
        """Reset configuration back to default values."""
        self._config = self._deep_copy(self._defaults)

    @property
    def data(self) -> Dict[str, Any]:
        """Return full current configuration dictionary."""
        return self._deep_copy(self._config)
