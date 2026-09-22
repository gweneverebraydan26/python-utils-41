# python-utils-41

A collection of lightweight, high-performance Python utilities designed to streamline common development tasks. This library focuses on reducing boilerplate code for file operations, data validation, and asynchronous task management.

## Features

*   **Robust File I/O:** Simplified wrappers for rapid directory traversal, pattern-based file searching, and atomic JSON serialization.
*   **Data Validation:** A lightweight set of decorators for schema validation and type-checking, minimizing runtime errors in production.
*   **Async Helpers:** Intuitive utility functions for batching asynchronous tasks and managing concurrent subprocesses with ease.
*   **String Formatting:** Optimized patterns for common data sanitization tasks, including slug generation and complex delimiter parsing.

## Installation

Install the package directly via pip:

```bash
pip install python-utils-41
```

Or add it to your `requirements.txt`:

```text
python-utils-41>=1.0.0
```

## Usage

Here is a quick example demonstrating how to use the file-caching utility to handle JSON storage:

```python
from pyutils41.io import json_cache

# Decorate a function to automatically cache output to a file
@json_cache(filename="data.json", ttl=3600)
def fetch_external_data():
    return {"status": "success", "payload": [1, 2, 3]}

# The first call fetches data, subsequent calls within an hour load from disk
data = fetch_external_data()
print(data['status'])
```

## Contributing

We welcome contributions! Please open an issue for feature requests or submit a pull request for bug fixes. Ensure all new code includes corresponding tests in the `tests/` directory.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.