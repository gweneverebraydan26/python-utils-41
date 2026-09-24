import os
import json
import logging
from typing import Any, Optional

def ensure_dir(path: str) -> None:
    """Creates directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def save_json(data: Any, filepath: str) -> None:
    """Serializes data to a JSON file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, sort_keys=True)

def load_json(filepath: str) -> Optional[Any]:
    """Loads data from a JSON file."""
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_env_var(key: str, default: str = '') -> str:
    """Retrieves environment variable with fallback."""
    return os.environ.get(key, default)

def setup_basic_logger(name: str) -> logging.Logger:
    """Configures a standard logger instance."""
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger