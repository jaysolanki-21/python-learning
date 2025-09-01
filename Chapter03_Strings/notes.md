# Chapter 3: Strings in Python

## 1. What is a String?
- A **string** is a sequence of characters enclosed in single (`'`), double (`"`), or triple quotes (`'''` or `"""`).
- Strings in Python are **immutable** → once created, they cannot be changed.

---

## 2. Ways to Define Strings
```python
str1 = 'Hello'        # Single quotes
str2 = "World"        # Double quotes
str3 = '''Multi-line
string'''             # Triple quotes
```

## 3. String Immutability
You cannot change individual characters directly.

```python
s = "Python"
# s[0] = 'J' ❌ Error
s = "Jython"  # ✅ Create a new string
```

## 4. String Slicing
Accessing parts of a string.

```python
s = "Python"
print(s[0:4])   # Pyth
print(s[:3])    # Pyt
print(s[2:])    # thon
```

### With Step/Skip Value
```python
s = "Python"
print(s[::2])   # Pto
print(s[::-1])  # Reverse → nohtyP
```

## 5. String Functions
```python
s = "python programming"

print(len(s))           # Length → 18
print(s.endswith("ing"))# True
print(s.startswith("py")) # True
print(s.capitalize())   # Python programming
print(s.lower())        # python programming
print(s.upper())        # PYTHON PROGRAMMING
print(s.title())        # Python Programming
print(s.find("pro"))    # 7 (index where found)
print(s.count("p"))     # 2
print(s.replace("python", "java")) # java programming
```

## 6. Escape Sequence Characters
```python
print("Hello\nWorld")  # Newline
print("Name\tAge")     # Tab space
print("He said, \"Hi\"")  # Double quotes inside
print("Path: C:\\Users")   # Backslash
```

✅ **Key Takeaways**

- Strings are immutable.
- Slicing lets you extract substrings.
- Many built-in functions for manipulation.
- Escape sequences handle special formatting.

---
