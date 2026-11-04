import os
from typing import Any, Dict

class AppConfig:
    """Centralized configuration management for the project."""

    def __init__(self, env_prefix: str = 'APP_'):
        self.env_prefix = env_prefix
        self.settings: Dict[str, Any] = {}
        self._load_defaults()
        self._load_from_env()

    def _load_defaults(self) -> None:
        """Initialize base default settings."""
        self.settings = {
            "LOG_LEVEL": "INFO",
            "MAX_RETRIES": 3,
            "TIMEOUT": 30,
            "DEBUG": False
        }

    def _load_from_env(self) -> None:
        """Override settings with environment variables."""
        for key in self.settings:
            env_var = f"{self.env_prefix}{key}"
            if env_var in os.environ:
                val = os.environ[env_var]
                # Basic type casting for standard config types
                if isinstance(self.settings[key], bool):
                    self.settings[key] = val.lower() in ('true', '1', 'yes')
                elif isinstance(self.settings[key], int):
                    self.settings[key] = int(val)
                else:
                    self.settings[key] = val

    def get(self, key: str, default: Any = None) -> Any:
        """Safe retrieval of configuration values."""
        return self.settings.get(key, default)

def get_config() -> AppConfig:
    """Factory function for global config instance."""
    return AppConfig()