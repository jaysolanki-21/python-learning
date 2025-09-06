
## Chapter 08: Functions & Recursion in Python

---

### 1. What is a Function?
A function is a block of code that performs a specific task and can be reused. Functions help organize code, reduce repetition, and improve readability.

**Syntax:**
```python
def function_name(parameters):
    # code block
    return value
```

---

### 2. Function Parameters & Arguments
- **Parameters**: Variables listed inside the parentheses in the function definition.
- **Arguments**: Values passed to the function when calling it.
- **Default Parameters**: Assign default values to parameters.

```python
def greet(name, msg="Hello"):
    print(msg, name)

greet("Alice")           # Output: Hello Alice
greet("Bob", "Hi")       # Output: Hi Bob
```

---

### 3. Return Statement
- Use `return` to send a result back to the caller.
- Functions without a return statement return `None`.

```python
def add(a, b):
    return a + b

result = add(2, 3)  # result = 5
```

---

### 4. Types of Functions
- **Built-in Functions**: Provided by Python (e.g., `print()`, `len()`).
- **User-defined Functions**: Created by the programmer.
- **Lambda Functions**: Anonymous, single-expression functions.

```python
square = lambda x: x * x
print(square(5))  # Output: 25
```

---

### 5. Recursion
Recursion is when a function calls itself to solve a problem.

**Key Points:**
- Must have a base case to avoid infinite recursion.
- Useful for problems that can be broken into similar subproblems (e.g., factorial, Fibonacci).

**Example: Factorial**
```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

---

### 6. Best Practices
- Use descriptive function names.
- Keep functions short and focused.
- Avoid deep recursion (can cause stack overflow).
- Document functions with docstrings.

**Example Docstring:**
```python
def add(a, b):
    """Return the sum of a and b."""
    return a + b
```

---

### 7. Common Pitfalls
- Forgetting the base case in recursion.
- Not returning a value when needed.
- Using mutable default arguments (e.g., lists).

---

### 8. Practice Problems
- Write a function to check if a number is prime.
- Write a recursive function to compute the nth Fibonacci number.
- Write a function to reverse a string.

---
