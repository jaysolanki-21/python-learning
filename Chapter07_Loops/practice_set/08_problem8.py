# Write a python script to print the following pattern for n number of rows.
n = int(input("Enter the number: "))
for i in range(1, n+1): 
    print("*"* i, end="")
    print("")