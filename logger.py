import logging
import sys
from typing import Optional

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Configures a standard logger instance for project modules."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger

def get_child_logger(parent: logging.Logger, suffix: str) -> logging.Logger:
    """Creates a hierarchical child logger from a parent."""
    return parent.getChild(suffix)

def log_exception(logger: logging.Logger, e: Exception, context: str = "") -> None:
    """Logs an exception with optional contextual information."""
    msg = f"Error occurred: {context}" if context else "Error occurred"
    logger.exception(f"{msg} - {str(e)}")