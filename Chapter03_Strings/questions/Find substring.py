s = input("Enter a string: ")
sub = input("Enter substring: ")
if sub in s:
    print(f"'{sub}' found at index", s.find(sub))
else:
    print("Not found")
