# Chapter 2: Variables, Data Types & Operators

---

## 1. Variables
- A **variable** is a container for storing data.
- Example:
  ```python
  x = 10
  name = "Alice"
  ```

## 2. Data Types
Common Python data types:

- `int` → whole numbers
- `float` → decimal numbers
- `str` → text/strings
- `bool` → True or False
- `list`, `tuple`, `set`, `dict`

**Example:**
```python
age = 21        # int
pi = 3.14       # float
name = "Jay"    # str
is_mca = True   # bool
```

## 3. Variable Naming Rules
**Allowed:**
- Must start with a letter or underscore (_)
- Can contain letters, numbers, and underscores

**Not allowed:**
- Cannot start with a number
- Cannot use reserved keywords (`if`, `for`, `class`)

**Examples:**
```python
my_var = 10     # valid
_var2 = 20      # valid
# 2var = 30     # ❌ invalid
# for = 40      # ❌ invalid
```

## 4. Operators
### Arithmetic Operators
`+  -  *  /  %  **  //`

**Example:**
```python
print(10 + 3)   # 13
print(10 % 3)   # 1
print(2 ** 3)   # 8 (power)
```

### Assignment Operators
`=   +=   -=   *=   /=   //=   %=`

**Example:**
```python
x = 5
x += 3   # x = x + 3 → 8
```

### Comparison Operators
`==   !=   >   <   >=   <=`

**Example:**
```python
print(10 > 5)   # True
```

### Logical Operators
`and   or   not`

**Example:**
```python
x = True
y = False
print(x and y)   # False
print(x or y)    # True
```

## 5. type() Function & Type Casting
- `type()` → returns the type of a variable

**Example:**
```python
x = 10
print(type(x))   # <class 'int'>
```

- Type Casting → converting between types

**Example:**
```python
a = "123"
b = int(a)       # str → int
print(b + 1)     # 124
```

## 6. input() Function
- Takes input from user as string

**Example:**
```python
name = input("Enter your name: ")
print("Hello", name)
```

- Convert to int:
```python
age = int(input("Enter your age: "))
print("You will be", age+1, "next year.")
```

---
