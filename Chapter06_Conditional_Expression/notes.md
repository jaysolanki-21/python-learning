
# Chapter 6: Conditional Expressions

---

## 1. `if` Statement
- Executes a block of code only when the condition is `True`.

**Example:**
```python
x = 10
if x > 5:
    print("x is greater than 5")
```

---

## 2. `if-else` Statement
- Provides an alternative block when the condition is `False`.

**Example:**
```python
age = 18
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
```

---

## 3. `if-elif-else` Ladder
- Checks multiple conditions in sequence. Once a condition is `True`, the rest are skipped.

**Example:**
```python
marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")
```

---

## 4. Relational Operators
- Used to compare two values.

| Operator | Meaning                  | Example (a=10, b=5) |
|----------|-------------------------|---------------------|
| ==       | Equal to                | a == b → False      |
| !=       | Not equal to            | a != b → True       |
| >        | Greater than            | a > b → True        |
| <        | Less than               | a < b → False       |
| >=       | Greater than or equal   | a >= b → True       |
| <=       | Less than or equal      | a <= b → False      |

---

## 5. Logical Operators
- Used to combine multiple conditions.

| Operator | Meaning           | Example                  |
|----------|------------------|--------------------------|
| and      | Both must be True| (a > 5 and b < 10) → True|
| or       | At least one True| (a < 5 or b < 10) → True |
| not      | Negates condition| not(a > 5) → False       |

---

## 6. `elif` Clause
- Used inside an if-elif-else structure. Short for "else if".

**Example:**
```python
num = 0
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```