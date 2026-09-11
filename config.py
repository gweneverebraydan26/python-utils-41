import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Loads JSON configuration with provided default values."""
    config = defaults.copy()

    if not os.path.exists(filepath):
        return config

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            if isinstance(data, dict):
                config.update(data)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def save_config(filepath: str, config: Dict[str, Any]) -> bool:
    """Persists current configuration dictionary to disk."""
    try:
        with open(filepath, 'w') as f:
            json.dump(config, f, indent=4)
        return True
    except IOError:
        return False