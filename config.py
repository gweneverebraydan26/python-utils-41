import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Handles loading configuration from JSON files with fallback defaults."""

    def __init__(self, default_config: Dict[str, Any] = None):
        self.defaults = default_config or {}

    def load(self, filepath: str) -> Dict[str, Any]:
        """Loads configuration from a file, merging with default values."""
        config = self.defaults.copy()
        
        if not os.path.exists(filepath):
            return config

        try:
            with open(filepath, 'r') as f:
                loaded_data = json.load(f)
                if isinstance(loaded_data, dict):
                    config.update(loaded_data)
        except (json.JSONDecodeError, IOError):
            # Return defaults if file is corrupt or unreadable
            pass
            
        return config

# Example Usage:
if __name__ == '__main__':
    defaults = {'host': 'localhost', 'port': 8080}
    loader = ConfigLoader(defaults)
    current_config = loader.load('config.json')
    print(f"Loaded config: {current_config}")