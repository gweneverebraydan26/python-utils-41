import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Utility for loading JSON configurations with defaults."""

    def __init__(self, default_config: Dict[str, Any]):
        self.config = default_config

    def load_from_file(self, filepath: str) -> None:
        """Overwrites default config with values from JSON file."""
        if not os.path.exists(filepath):
            return

        with open(filepath, 'r') as f:
            try:
                user_config = json.load(f)
                self.config.update(user_config)
            except json.JSONDecodeError:
                pass

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves value by key with optional fallback."""
        return self.config.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self.config[key]

# Example usage for python-utils-41
if __name__ == '__main__':
    defaults = {'host': 'localhost', 'port': 8080}
    loader = ConfigLoader(defaults)
    loader.load_from_file('settings.json')
    print(f"Active configuration: {loader.config}")