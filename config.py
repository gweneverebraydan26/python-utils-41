import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Handles loading and merging of configuration files with defaults."""
    
    def __init__(self, default_config: Dict[str, Any]):
        self.config = default_config

    def load_from_file(self, filepath: str) -> None:
        """Overwrites default config values with those found in the JSON file."""
        if not os.path.exists(filepath):
            return

        try:
            with open(filepath, 'r') as f:
                user_config = json.load(f)
                self.config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Configuration load error: {e}")

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key."""
        return self.config.get(key, default)

def get_app_config(config_path: str = "config.json") -> ConfigLoader:
    """Factory function for a standard configuration loader instance."""
    defaults = {
        "host": "localhost",
        "port": 8080,
        "debug": False
    }
    loader = ConfigLoader(defaults)
    loader.load_from_file(config_path)
    return loader