from typing import Any, Dict, Optional, Callable
import logging

logger = logging.getLogger(__name__)

class DataHandler:
    """Handles transformation and routing of processed data."""

    def __init__(self, prefix: str = "proc_") -> None:
        self.prefix: str = prefix
        self.registry: Dict[str, Callable] = {}

    def register_task(self, name: str, func: Callable[[Any], Any]) -> None:
        """Registers a processing function with a unique identifier."""
        self.registry[f"{self.prefix}{name}"] = func

    def execute(self, name: str, data: Any) -> Optional[Any]:
        """Executes a registered task if it exists."""
        task_key = f"{self.prefix}{name}"
        func = self.registry.get(task_key)
        
        if not func:
            logger.error(f"Task {task_key} not found in registry")
            return None
            
        try:
            return func(data)
        except Exception as e:
            logger.exception(f"Error executing task {task_key}: {e}")
            return None

    def list_tasks(self) -> list[str]:
        """Returns a list of all currently registered task names."""
        return list(self.registry.keys())