# python-utils-41

A collection of lightweight, high-performance Python utilities designed to streamline common data processing and system automation tasks. This library focuses on efficiency and developer ergonomics to minimize boilerplate in daily scripting workflows.

## Features

*   **Robust File Operations:** Advanced context managers for safe atomic file writes and recursive directory synchronization.
*   **Performance Decorators:** Pre-built timing and caching decorators to identify bottlenecks and optimize function execution speeds.
*   **Object Transformation:** Utility methods for deep-merging dictionaries and flattening complex nested data structures.
*   **Logging Enhancements:** Standardized formatting wrappers that enable multi-stream logging with color-coded severity levels out of the box.

## Installation

Install the package directly from PyPI using pip:

```bash
pip install python-utils-41
```

To install from source for local development:

```bash
git clone https://github.com/Developer/python-utils-41.git
cd python-utils-41
pip install -e .
```

## Usage

Here is a quick example of how to use the built-in execution timer to monitor function performance:

```python
from pyutils41.decorators import time_execution

@time_execution
def process_data(payload):
    # Simulate heavy computation
    return [i * 2 for i in payload]

result = process_data(range(1000000))
# Output: [Function: process_data] took 0.045s to execute.
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.