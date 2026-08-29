import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def configure_rotating_logger(
    logger_name: str = "app",
    log_file: str = "logs/app.log",
    max_size_mb: int = 10,
    backup_count: int = 5,
    log_level: int = logging.INFO
) -> logging.Logger:
    """Configure a logger with rotating file handler and console output.

    Creates the log directory if it doesn't exist.
    """
    logger = logging.getLogger(logger_name)
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.setLevel(log_level)

    # Ensure log directory exists
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    # Rotating file handler setup
    max_bytes = max_size_mb * 1024 * 1024
    file_handler = RotatingFileHandler(
        filename=str(log_path),
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8"
    )
    file_handler.setLevel(log_level)

    # Console handler for immediate feedback
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    # Common formatter
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.info("Rotating logger configured successfully")
    return logger

# Example usage
if __name__ == "__main__":
    app_logger = configure_rotating_logger(
        logger_name="python-utils",
        log_file="logs/utils.log",
        max_size_mb=5,
        backup_count=3
    )
    app_logger.info("Application started")
    app_logger.warning("This is a warning message")
    app_logger.error("Example error for testing")
    # Simulate many messages
    for i in range(100):
        app_logger.debug(f"Debug message number {i}")
