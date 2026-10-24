import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

def safe_execute(func: callable, *args: Any, **kwargs: Any) -> Optional[Any]:
    """
    Executes a callable with error handling for edge cases.
    Handles potential crashes during execution and logs outcomes.
    """
    if not callable(func):
        logger.error(f"Provided object {type(func)} is not callable")
        return None

    try:
        return func(*args, **kwargs)
    except TypeError as e:
        logger.error(f"Signature mismatch in function execution: {e}")
    except ValueError as e:
        logger.warning(f"Invalid input arguments provided: {e}")
    except Exception as e:
        logger.exception(f"Unexpected error occurred: {e}")
    
    return None

def validate_data(data: Any) -> bool:
    """
    Validates presence and type of data inputs.
    """
    if data is None:
        logger.debug("Received null data packet")
        return False
    
    if not isinstance(data, (dict, list, str)):
        logger.warning(f"Unsupported data structure type: {type(data)}")
        return False
        
    return True