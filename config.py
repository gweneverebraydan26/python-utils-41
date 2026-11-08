import json
import os
from pathlib import Path
from typing import Any, Dict, Optional, Union

DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "python-utils",
    "version": "1.0.0",
    "debug": False,
    "port": 8080,
    "log_level": "INFO",
    "max_retries": 3,
}


class ConfigLoader:
    """Utility class to load and merge configuration settings with defaults."""

    def __init__(self, default_config: Optional[Dict[str, Any]] = None):
        self.defaults = (
            default_config.copy()
            if default_config is not None
            else DEFAULT_CONFIG.copy()
        )

    def load_from_json(self, file_path: Union[str, Path]) -> Dict[str, Any]:
        """Load configuration from a JSON file, falling back to defaults."""
        config = self.defaults.copy()
        path = Path(file_path)

        if not path.exists():
            return config

        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    config.update(data)
        except (json.JSONDecodeError, OSError):
            pass

        return config

    def apply_env_overrides(
        self, config: Dict[str, Any], prefix: str = "APP_"
    ) -> Dict[str, Any]:
        """Override configuration values using matching environment variables."""
        result = config.copy()
        for key, default_val in result.items():
            env_key = f"{prefix}{key.upper()}"
            if env_key in os.environ:
                raw_val = os.environ[env_key]
                if isinstance(default_val, bool):
                    result[key] = raw_val.lower() in ("true", "1", "yes")
                elif isinstance(default_val, int):
                    try:
                        result[key] = int(raw_val)
                    except ValueError:
                        pass
                else:
                    result[key] = raw_val
        return result


def load_config(
    config_path: Optional[Union[str, Path]] = None,
    env_prefix: str = "APP_",
    defaults: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Load configuration from JSON file with env overrides and default values."""
    loader = ConfigLoader(default_config=defaults)
    if config_path:
        cfg = loader.load_from_json(config_path)
    else:
        cfg = loader.defaults.copy()

    return loader.apply_env_overrides(cfg, prefix=env_prefix)
