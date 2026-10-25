[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# python-utils-41

`python-utils-41` is a lightweight, zero-dependency Python library designed to streamline common data manipulation, file handling, and execution tasks. It provides clean, performant helper functions that eliminate repetitive boilerplate code across your backend services and automation scripts.

## Features

- **Smart Dictionary Merging**: Deep-merge nested dictionaries with configurable strategies for list handling and key collisions.
- **Atomic File Operations**: Thread-safe, atomic read/write functions to prevent file corruption during execution failures.
- **Exponential Retry Decorator**: Configurable function retry logic with customizable backoff timers for unstable network calls.
- **String Normalization**: Fast unicode sanitization and slug generator optimized for data pipelines and web routes.

## Installation

Install the package via `pip`:

```bash
pip install python-utils-41
```

For development installations from source:

```bash
git clone https://github.com/Developer/python-utils-41.git
cd python-utils-41
pip install -e .
```

## Basic Usage

```python
from python_utils_41 import deep_merge, safe_write_json, retry

# Safely merge nested configuration objects
default_config = {"database": {"host": "localhost", "port": 5432}, "retries": 3}
user_config = {"database": {"port": 5433}}

final_config = deep_merge(default_config, user_config)

# Atomic JSON export
safe_write_json("config.json", final_config)

# Decorate unreliable network calls with auto-retry logic
@retry(max_attempts=3, delay=1.5, backoff=2.0)
def fetch_api_data():
    # Your API request logic here
    pass
```

## License

Distributed under the MIT License. Created by Developer.