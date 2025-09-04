# Chapter 6 - Conditional Expressions Examples

# Example 1: if statement
x = 10
if x > 5:
    print("x is greater than 5")

# Example 2: if else
age = 18
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# Example 3: if elif ladder
marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")

# Example 4: Relational operators
a, b = 10, 5
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Example 5: Logical operators
print("a > 5 and b < 10:", a > 5 and b < 10)
print("a < 5 or b < 10:", a < 5 or b < 10)
print("not(a > 5):", not(a > 5))

# Example 6: elif clause
num = 0
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")