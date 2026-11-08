import logging
import sys
from typing import Optional

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Configures a standard logger with a stream handler."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
    return logger

class LoggerMixin:
    """Mixin class to provide logging capabilities to classes."""
    @property
    def logger(self) -> logging.Logger:
        return logging.getLogger(self.__class__.__name__)

def get_default_logger() -> logging.Logger:
    """Helper for quick module-level access to logger."""
    return setup_logger("python-utils-41")