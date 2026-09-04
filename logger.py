import logging
import sys
from typing import Optional

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Configures and returns a standardized application logger."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

class AppLogger:
    """Wrapper class for centralized logging operations."""
    def __init__(self, name: str):
        self.logger = get_logger(name)

    def info(self, msg: str) -> None:
        self.logger.info(msg)

    def error(self, msg: str, exc_info: bool = True) -> None:
        self.logger.error(msg, exc_info=exc_info)

    def debug(self, msg: str) -> None:
        self.logger.debug(msg)