import json
import os
from typing import Any, Dict

def load_config(path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Loads JSON config file and merges with provided defaults."""
    config = defaults.copy()
    
    if not os.path.exists(path):
        return config

    try:
        with open(path, 'r') as f:
            data = json.load(f)
            if isinstance(data, dict):
                config.update(data)
    except (json.JSONDecodeError, IOError):
        pass
        
    return config

def get_env_var(key: str, default: str) -> str:
    """Retrieves environment variable with fallback."""
    return os.environ.get(key, default)

# Usage example for configuration management
if __name__ == "__main__":
    default_settings = {
        "host": "127.0.0.1",
        "port": 8080,
        "debug": False
    }
    
    settings = load_config("config.json", default_settings)
    print(f"Loaded settings: {settings}")