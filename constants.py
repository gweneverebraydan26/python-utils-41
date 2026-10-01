from typing import Final, Dict, List

# Application-wide configuration constants

DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

SUPPORTED_ENCODINGS: Final[List[str]] = ['utf-8', 'ascii', 'latin-1']

ERROR_MESSAGES: Final[Dict[int, str]] = {
    400: 'bad request syntax',
    401: 'unauthorized access attempt',
    403: 'forbidden resource access',
    404: 'resource not found',
    500: 'internal server error'
}

def get_error_message(status_code: int) -> str:
    """
    Retrieve a human-readable message for a given HTTP status code.

    Args:
        status_code: The integer status code to look up.

    Returns:
        A string description of the error or a generic message if unknown.
    """
    return ERROR_MESSAGES.get(status_code, 'unknown error occurred')

class ConfigDefaults:
    """
    Namespace for nested configuration default settings.
    """
    LOG_LEVEL: Final[str] = 'INFO'
    BATCH_SIZE: Final[int] = 100
    ENABLE_DEBUG: Final[bool] = False