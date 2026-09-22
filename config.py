import os
import json
from typing import Any, Dict

def load_config(file_path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Loads configuration from a JSON file with specified default values.
    """
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

def get_env_config(prefix: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Loads configuration from environment variables prefixed with the given string.
    """
    config = defaults.copy()
    for key in defaults.keys():
        env_key = f"{prefix}_{key.upper()}"
        value = os.environ.get(env_key)
        if value is not None:
            # Attempt simple type casting based on default type
            default_val = defaults[key]
            if isinstance(default_val, bool):
                config[key] = value.lower() in ('true', '1', 'yes')
            elif isinstance(default_val, int):
                config[key] = int(value)
            else:
                config[key] = value
    return config