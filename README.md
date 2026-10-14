# python-utils-41

A collection of lightweight, high-performance utility functions designed to streamline daily Python development tasks. This library focuses on reducing boilerplate code for common data manipulation, file system operations, and performance benchmarking.

## Features

*   **Dynamic Data Sanitization:** Robust tools for cleaning nested dictionaries and converting complex types, ensuring API payloads are always schema-compliant.
*   **Enhanced File Handling:** Simplified context managers for recursive directory traversal and atomic file writing to prevent data corruption.
*   **Execution Profiling:** A decorator-based suite for tracking function execution time and memory footprint with minimal overhead.
*   **Zero-Dependency Core:** Built using only Python standard libraries to ensure maximum compatibility across restricted environments.

## Installation

Install `python-utils-41` directly via pip:

```bash
pip install python-utils-41
```

Or add it to your `requirements.txt`:

```text
python-utils-41>=1.0.0
```

## Basic Usage

Import the utilities to automate repetitive tasks like timing expensive functions or deep-merging dictionaries:

```python
from pyutils41.benchmarking import time_execution
from pyutils41.dict_ops import deep_merge

# Profile your functions with a simple decorator
@time_execution
def process_data(data):
    # Logic here
    return data

# Deep merge configuration dictionaries
base_config = {"api": {"retries": 3, "timeout": 30}}
user_config = {"api": {"timeout": 60}}

final_config = deep_merge(base_config, user_config)
print(final_config) 
# Output: {'api': {'retries': 3, 'timeout': 60}}
```

## Contributing

Contributions are welcome! Please open an issue to discuss proposed changes or submit a pull request for bug fixes. Ensure all code passes existing tests via `pytest` before submission.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.