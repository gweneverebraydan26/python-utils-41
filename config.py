import json
import os
from typing import Any, Dict, Optional


class ConfigError(Exception):
    """Base exception raised for configuration loading errors."""
    pass


class ConfigLoader:
    """Loads and validates application configuration settings safely."""

    def __init__(self, default_config: Optional[Dict[str, Any]] = None) -> None:
        self._config: Dict[str, Any] = default_config.copy() if default_config else {}

    def load_from_file(self, filepath: str) -> Dict[str, Any]:
        """Loads configuration from a JSON file with edge-case handling."""
        if not isinstance(filepath, str) or not filepath.strip():
            raise ConfigError("Filepath must be a non-empty string")

        if not os.path.exists(filepath):
            raise ConfigError(f"Configuration file not found: {filepath}")

        if not os.path.isfile(filepath):
            raise ConfigError(f"Specified path is not a file: {filepath}")

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                if not isinstance(data, dict):
                    raise ConfigError("Root configuration structure must be a JSON object")
                self._config.update(data)
        except json.JSONDecodeError as err:
            raise ConfigError(f"Invalid JSON format in {filepath}: {err.msg}") from err
        except (PermissionError, OSError) as err:
            raise ConfigError(f"Failed to read file {filepath}: {str(err)}") from err

        return self._config

    def get_env_override(self, key: str, env_var: str, cast_type: Optional[type] = None) -> Any:
        """Safely applies an environment variable override with type casting."""
        value = os.getenv(env_var)
        if value is None:
            return self._config.get(key)

        if cast_type is bool:
            lower_val = value.strip().lower()
            if lower_val in ("true", "1", "yes", "on"):
                typed_val = True
            elif lower_val in ("false", "0", "no", "off"):
                typed_val = False
            else:
                raise ConfigError(f"Cannot cast env var '{env_var}' value '{value}' to bool")
        elif cast_type is not None:
            try:
                typed_val = cast_type(value)
            except (ValueError, TypeError) as err:
                raise ConfigError(f"Failed to cast env var '{env_var}' ({value}) to {cast_type.__name__}") from err
        else:
            typed_val = value

        self._config[key] = typed_val
        return typed_val