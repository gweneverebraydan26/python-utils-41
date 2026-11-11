import json
import os
from typing import Any, Dict

def load_config(path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Loads configuration from a JSON file with specified defaults.
    Returns the merged configuration dictionary.
    """
    config = defaults.copy()

    if not os.path.exists(path):
        return config

    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, dict):
                config.update(data)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def save_config(path: str, config: Dict[str, Any]) -> None:
    """
    Persists the current configuration dictionary to a JSON file.
    """
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4)

if __name__ == '__main__':
    # Example usage for python-utils-41
    defaults = {'debug': False, 'port': 8080, 'host': 'localhost'}
    loaded = load_config('settings.json', defaults)
    print(f'Loaded config: {loaded}')