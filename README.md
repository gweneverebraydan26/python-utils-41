# python-utils-41

A collection of lightweight, high-performance Python utilities designed to streamline daily automation and data processing tasks. This library focuses on reducing boilerplate code for common file system operations, text manipulation, and execution timing.

## Features

*   **Robust File Operations:** Simplified wrappers for recursive file searching, batch renaming, and bulk file-type conversion.
*   **Performance Profiling:** A decorator-based execution timer to track function latency with millisecond precision and logging support.
*   **String Sanitization:** Native support for slugifying complex strings and stripping non-printable characters for clean data ingestion.
*   **Memory-Efficient Iterators:** Lazy-loading utilities for processing massive CSV and JSON files without exhausting system RAM.

## Installation

Install the package directly via pip:

```bash
pip install python-utils-41
```

Or, if you are working within a virtual environment, ensure your requirements file is updated:

```bash
echo "python-utils-41" >> requirements.txt
pip install -r requirements.txt
```

## Usage

Utilize the performance decorator to monitor function execution time or use the file utilities to manage your workspace efficiently:

```python
from pyutils41.profiler import time_execution
from pyutils41.files import get_files_by_extension

# Monitor function performance
@time_execution(logger=print)
def process_data(data):
    # Process logic here
    return len(data)

# Quickly find all logs in a directory
logs = get_files_by_extension("./logs", ".log")
print(f"Found {len(logs)} log files.")
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.