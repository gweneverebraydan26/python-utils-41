import json
import os
from pathlib import Path
from typing import Any, Dict, Optional, Union


class ConfigLoader:
    """Utility for loading configuration files with default fallbacks."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None):
        self.defaults = defaults or {}

    def _deep_merge(self, base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
        """Recursively merge override dictionary into base dictionary."""
        merged = base.copy()
        for key, value in override.items():
            if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
                merged[key] = self._deep_merge(merged[key], value)
            else:
                merged[key] = value
        return merged

    def load_from_json(self, filepath: Union[str, Path]) -> Dict[str, Any]:
        """Load configuration from a JSON file, applying default values."""
        config_path = Path(filepath)
        if not config_path.exists():
            return self.defaults.copy()

        try:
            with open(config_path, "r", encoding="utf-8") as f:
                file_config = json.load(f)
        except (json.JSONDecodeError, OSError) as err:
            raise ValueError(f"Failed to parse config file '{filepath}': {err}")

        return self._deep_merge(self.defaults, file_config)

    def load_from_env(self, prefix: str = "APP_") -> Dict[str, Any]:
        """Extract environment variables matching a prefix into a dictionary."""
        env_config: Dict[str, Any] = {}
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix):].lower()
                env_config[config_key] = value
        return self._deep_merge(self.defaults, env_config)
