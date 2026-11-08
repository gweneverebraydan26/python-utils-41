[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# python-utils-41

`python-utils-41` is a lightweight, zero-dependency Python toolkit designed to streamline common data processing, file system tasks, and functional workflows. It eliminates repetitive boilerplate across your projects by providing battle-tested helpers for dictionary manipulation, text normalization, and execution control.

## Features

- **Performance & Control Decorators:** Built-in timers, memoization helpers, and automatic retries with exponential backoff for flaky operations.
- **Deep Dictionary Operations:** Utilities for recursive dictionary merging, key flattening, and safe dot-notation paths for nested structures.
- **Text & Slug Processing:** High-performance text normalization, advanced slugification, and seamless case conversion (camelCase, snake_case, kebab-case).
- **Atomic File Handling:** Safe file writing wrappers, directory tree management, and fast JSON/YAML file operations.

## Installation

Install the package directly via `pip`:

```bash
pip install python-utils-41
```

Or build from source:

```bash
git clone https://github.com/Developer/python-utils-41.git
cd python-utils-41
pip install .
```

## Quick Start

```python
from python_utils_41.decorators import retry
from python_utils_41.dicts import deep_merge
from python_utils_41.strings import slugify

# Retry an operation up to 3 times with exponential backoff
@retry(max_attempts=3, delay=1.0, backoff_factor=2.0)
def connect_to_service():
    # Simulation of a network call
    return {"status": "connected"}

# Merge nested configurations safely
base_config = {"database": {"host": "localhost", "port": 5432}}
override_config = {"database": {"port": 5433, "user": "admin"}}
final_config = deep_merge(base_config, override_config)

# Generate URL-friendly slugs
clean_url = slugify("Release v1.0: New Features & Bug Fixes!")
print(clean_url)  # Output: release-v10-new-features-and-bug-fixes
```

## License

Distributed under the MIT License. See `LICENSE` for more information.