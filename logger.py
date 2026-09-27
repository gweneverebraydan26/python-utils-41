import logging
import os
from logging.handlers import RotatingFileHandler
from typing import Optional

def get_rotated_logger(
    name: str,
    log_file: str,
    max_bytes: int = 10485760,  # 10 MB
    backup_count: int = 5,
    level: int = logging.INFO,
    console_output: bool = True
) -> logging.Logger:
    """
    Configures and returns a logger with a rotating file handler and optional console output.
    
    Ensures log directories exist and avoids duplicating handlers if the logger
    is already initialized.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent handler duplication
    if logger.handlers:
        return logger

    # Standard log format
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Create directory for log files if it does not exist
    log_dir = os.path.dirname(log_file)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)

    # Set up rotating file handler
    file_handler = RotatingFileHandler(
        filename=log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)
    logger.addHandler(file_handler)

    # Optionally add standard output stream handler
    if console_output:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(level)
        logger.addHandler(console_handler)

    return logger
