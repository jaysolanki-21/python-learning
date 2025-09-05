# Chapter 7: Loops Examples

# 1. For loop
print("For loop (0 to 4):")
for i in range(5):
    print(i)

print("\n")

# 2. While loop
print("While loop (count down from 5):")
count = 5
while count > 0:
    print(count)
    count -= 1

print("\n")

# 3. Iterate over list
fruits = ["apple", "banana", "cherry"]
print("Iterating over list:")
for fruit in fruits:
    print(fruit)

print("\n")

# 4. Iterate over tuple
numbers = (10, 20, 30)
print("Iterating over tuple:")
for num in numbers:
    print(num)

print("\n")

# 5. For loop with else
print("For loop with else:")
for i in range(3):
    print(i)
else:
    print("Loop completed!")

print("\n")

# 6. Break statement
print("Using break:")
for i in range(10):
    if i == 5:
        break
    print(i)

print("\n")

# 7. Continue statement
print("Using continue (skip 5):")
for i in range(10):
    if i == 5:
        continue
    print(i)

print("\n")

# 8. Pass statement
print("Using pass (do nothing for 5):")
for i in range(10):
    if i == 5:
        pass
    print(i)
