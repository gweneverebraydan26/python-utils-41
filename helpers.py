import json
import os
from typing import Any, Dict

def load_config(file_path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Loads configuration from a JSON file with provided defaults."""
    config = defaults.copy()
    
    if not os.path.exists(file_path):
        return config
        
    try:
        with open(file_path, 'r') as f:
            user_config = json.load(f)
            if isinstance(user_config, dict):
                config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass
        
    return config

def save_config(file_path: str, config: Dict[str, Any]) -> None:
    """Saves configuration dictionary to a JSON file."""
    with open(file_path, 'w') as f:
        json.dump(config, f, indent=4)