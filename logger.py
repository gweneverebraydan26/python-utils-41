import logging
import os
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
from typing import Optional


def setup_logger(
    name: str = "app",
    log_file: Optional[str] = None,
    level: int = logging.INFO,
    max_bytes: int = 10 * 1024 * 1024,
    backup_count: int = 5,
    rotation_type: str = "size",
    fmt: Optional[str] = None,
) -> logging.Logger:
    """Configures and returns a logger instance with optional file rotation."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Clear existing handlers to prevent duplicate logging entries
    if logger.hasHandlers():
        logger.handlers.clear()

    if fmt is None:
        fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(fmt)

    # Set up stdout console logging
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Configure rotating file logging if a target file path is given
    if log_file:
        log_dir = os.path.dirname(log_file)
        if log_dir:
            os.makedirs(log_dir, exist_ok=True)

        if rotation_type == "time":
            file_handler = TimedRotatingFileHandler(
                log_file, when="midnight", interval=1, backupCount=backup_count
            )
        else:
            file_handler = RotatingFileHandler(
                log_file, maxBytes=max_bytes, backupCount=backup_count
            )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
