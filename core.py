import logging
from typing import Any, Callable, TypeVar, Optional, Union

logger = logging.getLogger(__name__)

T = TypeVar("T")


def safe_execute(
    func: Callable[..., T],
    *args: Any,
    default: Optional[T] = None,
    exceptions: Union[type[Exception], tuple[type[Exception], ...]] = Exception,
    **kwargs: Any,
) -> Optional[T]:
    """Execute a callable safely, catching specified exceptions and returning a default value."""
    try:
        return func(*args, **kwargs)
    except exceptions as err:
        logger.warning(
            "Safely caught exception during function execution: %s", err, exc_info=True
        )
        return default


def get_nested(data: dict[str, Any], keys: list[str], default: Any = None) -> Any:
    """Safely retrieve a nested value from a dictionary with edge-case handling."""
    if not isinstance(data, dict):
        return default

    current: Any = data
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]

    return current
