
# Chapter 7: Loops

---

## 1. For Loop
- Used to iterate over a sequence (list, tuple, string, range).

**Example:**
```python
for i in range(5):
    print(i)
# Output: 0 1 2 3 4
```

---

## 2. While Loop
- Runs as long as the condition is `True`.

**Example:**
```python
count = 5
while count > 0:
    print(count)
    count -= 1
# Output: 5 4 3 2 1
```

---

## 3. Iterating Over List
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output: apple banana cherry
```

---

## 4. Iterating Over Tuple
```python
numbers = (10, 20, 30)
for num in numbers:
    print(num)
# Output: 10 20 30
```

---

## 5. For Loop with Else
- The `else` block executes after the loop completes normally (not when stopped by `break`).

**Example:**
```python
for i in range(3):
    print(i)
else:
    print("Loop finished!")
# Output: 0 1 2 Loop finished!
```

---

## 6. Break Statement
- Exits the loop immediately.

**Example:**
```python
for i in range(10):
    if i == 5:
        break
    print(i)
# Output: 0 1 2 3 4
```

---

## 7. Continue Statement
- Skips the current iteration and continues with the next.

**Example:**
```python
for i in range(10):
    if i == 5:
        continue
    print(i)
# Output: 0 1 2 3 4 6 7 8 9
```

---

## 8. Pass Statement
- A placeholder, does nothing (useful for future code).

**Example:**
```python
for i in range(10):
    if i == 5:
        pass
    print(i)
# Output: 0 1 2 3 4 5 6 7 8 9
```