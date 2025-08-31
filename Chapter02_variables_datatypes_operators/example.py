# Chapter 2 Examples

# 1. Variables
x = 10
name = "Alice"
print(x, name)

# 2. Data Types
age = 21
pi = 3.14
is_student = True
print(type(age), type(pi), type(is_student))

# 3. Variable Rules
my_var = 100
_var2 = 200
print(my_var, _var2)

# 4. Operators
print("Arithmetic:", 10 + 5, 10 % 3, 2 ** 3)
x = 5
x += 2
print("Assignment:", x)
print("Comparison:", 10 > 5, 10 == 5)
print("Logical:", True and False, True or False, not True)

# 5. type() and Type Casting
num = "123"
print("Before casting:", type(num))
num = int(num)
print("After casting:", type(num), num + 1)

# 6. input()
name = input("Enter your name: ")
print("Hello", name)
