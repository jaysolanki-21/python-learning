
# 📘 Chapter 1: Modules, Comments & pip

## 1. Modules

A module is a file containing Python code (functions, classes, or variables).

Helps in code reusability and organization.

**Two types:**

- **Built-in modules** (already available in Python, e.g., `math`, `os`, `random`)
- **External modules** (installed via pip, e.g., `requests`, `numpy`)

**Example:**
```python
import math
print(math.sqrt(16))  # Output: 4.0

import random
print(random.randint(1, 10))  # Random number between 1–10
```

## 2. Comments

Comments are ignored by the Python interpreter.

Used for documentation, readability, and debugging.

**Types of Comments:**

- **Single-line comment**
	```python
	# This is a single-line comment
	```

- **Multi-line comment**
	```python
	"""
	This is a 
	multi-line comment
	"""
	```

## 3. pip

`pip` → Python’s package installer.

Allows us to install and manage external libraries.

**Common Commands:**
```bash
# Install a package
pip install requests

# Check installed packages
pip list

# Upgrade a package
pip install --upgrade requests

# Uninstall a package
pip uninstall requests
```
