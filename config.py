import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Handles configuration loading with file defaults."""

    def __init__(self, default_path: str = "config.json"):
        self.default_path = default_path
        self.config: Dict[str, Any] = {}

    def load(self, override_path: str = None) -> Dict[str, Any]:
        """Loads config from file or environment defaults."""
        path = override_path or self.default_path
        
        if not os.path.exists(path):
            return self._load_environment_defaults()

        with open(path, "r") as f:
            self.config = json.load(f)
        
        return self.config

    def _load_environment_defaults(self) -> Dict[str, Any]:
        """Extracts base settings from system environment."""
        return {
            "debug": os.getenv("DEBUG", "false").lower() == "true",
            "port": int(os.getenv("PORT", 8080)),
            "host": os.getenv("HOST", "127.0.0.1")
        }

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves value with fallback mechanism."""
        return self.config.get(key, default)