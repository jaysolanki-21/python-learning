# Write a python script to print the multiplication table of a given number
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} X {i} = {n * i}")