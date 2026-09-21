import logging
from typing import Optional

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Configures and returns a named logger instance.

    Args:
        name: Unique identifier for the logger.
        level: Logging threshold level.

    Returns:
        A configured logging.Logger object.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

def log_message(logger: logging.Logger, message: str, level: str = "info") -> None:
    """
    Logs a message at the specified severity level.

    Args:
        logger: The logging instance to use.
        message: The text string to log.
        level: Severity level (info, warning, error).
    """
    levels = {
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR
    }
    logger.log(levels.get(level.lower(), logging.INFO), message)