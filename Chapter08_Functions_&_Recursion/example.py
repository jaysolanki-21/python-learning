# Chapter 8: Functions and Recursion

# 1. Simple function
def greet():
    print("Hello, welcome to Python!")

greet()

# 2. Function with arguments
def add(a, b):
    return a + b

print("Sum of 5 and 3 is:", add(5, 3))

# 3. Function with default argument
def power(base, exp=2):
    return base ** exp

print("Square of 4 is:", power(4))      # uses default exp = 2
print("4 raised to power 3 is:", power(4, 3))

# 4. Recursion example: factorial
def factorial(n):
    if n == 0 or n == 1:  # base case
        return 1
    return n * factorial(n - 1)  # recursive call

print("Factorial of 5 is:", factorial(5))
