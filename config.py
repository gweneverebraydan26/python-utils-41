import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Handles configuration loading from JSON files with fallback defaults."""

    def __init__(self, default_config: Dict[str, Any] = None):
        self.defaults = default_config or {}

    def load(self, filepath: str) -> Dict[str, Any]:
        """Loads configuration from a JSON file, merging with defaults."""
        config = self.defaults.copy()

        if not os.path.exists(filepath):
            return config

        try:
            with open(filepath, 'r') as f:
                file_data = json.load(f)
                if isinstance(file_data, dict):
                    config.update(file_data)
        except (json.JSONDecodeError, IOError):
            pass

        return config

def get_app_config(filepath: str, defaults: Dict[str, Any] = None) -> Dict[str, Any]:
    """Utility function for quick configuration initialization."""
    loader = ConfigLoader(defaults)
    return loader.load(filepath)