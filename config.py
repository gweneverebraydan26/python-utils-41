import os
from typing import Any, Optional

class AppConfig:
    """Centralized configuration management for application settings."""

    def __init__(self, env_prefix: str = 'APP_') -> None:
        self.env_prefix = env_prefix
        self._settings = self._load_env_variables()

    def _load_env_variables(self) -> dict[str, str]:
        """Extract environment variables matching the prefix."""
        return {
            key[len(self.env_prefix):]: value
            for key, value in os.environ.items()
            if key.startswith(self.env_prefix)
        }

    def get(self, key: str, default: Any = None) -> Optional[Any]:
        """Retrieve setting value with optional default fallback."""
        return self._settings.get(key, default)

    def get_int(self, key: str, default: int = 0) -> int:
        """Retrieve setting value as an integer."""
        value = self.get(key)
        try:
            return int(value) if value is not None else default
        except (ValueError, TypeError):
            return default

    def get_bool(self, key: str, default: bool = False) -> bool:
        """Retrieve setting value as a boolean."""
        value = self.get(key)
        if value is None:
            return default
        return str(value).lower() in ('true', '1', 't', 'yes')

# Global config instance for application wide access
settings = AppConfig()