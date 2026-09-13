import time
import urllib.error
import urllib.request
from typing import Callable, Any, Optional

def fetch_with_retry(
    url: str,
    max_retries: int = 3,
    backoff_factor: float = 1.0,
    timeout: float = 5.0
) -> Optional[bytes]:
    """
    Fetch content from a URL with exponential backoff retry logic.
    """
    attempt = 0
    while attempt < max_retries:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'python-utils/1.0'})
            with urllib.request.urlopen(req, timeout=timeout) as response:
                return response.read()
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            attempt += 1
            if attempt >= max_retries:
                raise RuntimeError(f"Failed to fetch {url} after {max_retries} attempts") from e
            sleep_time = backoff_factor * (2 ** (attempt - 1))
            time.sleep(sleep_time)
    return None

def retry_operation(func: Callable[..., Any], max_retries: int = 3, backoff_factor: float = 1.0) -> Callable[..., Any]:
    """
    Decorator to retry any network operation upon failure.
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        attempt = 0
        while attempt < max_retries:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                attempt += 1
                if attempt >= max_retries:
                    raise e
                time.sleep(backoff_factor * (2 ** (attempt - 1)))
    return wrapper
