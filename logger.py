import os
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(
    name: str = "app",
    log_file: str = "logs/app.log",
    level: int = logging.INFO,
    max_bytes: int = 5 * 1024 * 1024,
    backup_count: int = 5,
    log_to_console: bool = True
) -> logging.Logger:
    """
    Configures and returns a logger with rotating file handler and optional console output.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if the logger is configured multiple times
    if logger.handlers:
        return logger

    # Ensure directory exists before creating log file
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    # Shared log record formatter
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    try:
        # Set up rotating file handler
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8"
        )
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level)
        logger.addHandler(file_handler)
    except (IOError, OSError) as error:
        # Fallback console warning if logging system directory is unwritable
        import sys
        print(f"Warning: Failed to setup file logger: {error}", file=sys.stderr)

    # Set up console handler if requested
    if log_to_console:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(level)
        logger.addHandler(console_handler)

    return logger