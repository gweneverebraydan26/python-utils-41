import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Handles configuration loading from JSON files with defaults."""

    def __init__(self, default_config: Dict[str, Any]):
        self._defaults = default_config

    def load(self, file_path: str) -> Dict[str, Any]:
        """Loads config from file, merging with defaults."""
        config = self._defaults.copy()
        
        if not os.path.exists(file_path):
            return config

        try:
            with open(file_path, 'r') as f:
                file_data = json.load(f)
                config.update(file_data)
        except (json.JSONDecodeError, IOError):
            pass
            
        return config

# Usage example
if __name__ == '__main__':
    defaults = {"host": "localhost", "port": 8080, "debug": False}
    loader = ConfigLoader(defaults)
    current_config = loader.load("config.json")
    print(f"Active config: {current_config}")