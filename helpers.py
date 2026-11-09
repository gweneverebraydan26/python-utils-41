import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Loads configuration from a JSON file, merging with provided defaults.
    """
    config = defaults.copy()
    
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r') as f:
                file_data = json.load(f)
                if isinstance(file_data, dict):
                    config.update(file_data)
        except (json.JSONDecodeError, IOError):
            pass
            
    return config

def save_config(filepath: str, config: Dict[str, Any]) -> bool:
    """
    Saves configuration dictionary to a JSON file.
    """
    try:
        with open(filepath, 'w') as f:
            json.dump(config, f, indent=4)
        return True
    except IOError:
        return False