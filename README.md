# python-utils-41

A collection of lightweight, high-performance Python utilities designed to streamline repetitive development tasks. This library bridges common functional gaps in standard library workflows, focusing on performance and code readability.

## Features

*   **Robust File Operations:** Advanced wrappers for recursive file processing, bulk renaming, and structured directory scanning.
*   **Dict-to-Object Mapper:** A zero-dependency utility to cast nested dictionaries into dot-notation accessible objects.
*   **Performance Decorators:** Pre-built function wrappers for intelligent caching, execution timing, and retry logic with exponential backoff.
*   **Type-Safe Converters:** Strict data transformers for complex JSON-to-CSV exports and environmental variable normalization.

## Installation

Install `python-utils-41` directly via pip:

```bash
pip install python-utils-41
```

Or add it to your `requirements.txt`:

```text
python-utils-41>=1.0.0
```

## Usage Example

Import the core modules to simplify your daily workflow:

```python
from pyutils41 import Mapper, Timer

# Map dictionaries to objects
data = {"user": {"id": 41, "name": "Admin"}}
user = Mapper.to_obj(data)
print(user.user.name)  # Output: Admin

# Time your function execution
@Timer.log
def process_data():
    return [i**2 for i in range(1000)]

process_data() 
# Logs: 'process_data' finished in 0.00012s
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.