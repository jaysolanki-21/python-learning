# Chapter 3: Strings Examples

# Defining strings
s1 = 'Hello'
s2 = "World"
s3 = '''This is
a multi-line string'''
print(s1, s2, s3)

# String immutability
s = "Python"
# s[0] = "J"  # ❌ Error
s = "Jython"
print(s)

# Slicing
text = "Programming"
print(text[0:6])   # Progra
print(text[:4])    # Prog
print(text[3:])    # gramming
print(text[::-1])  # Reverse

# Functions
msg = "python programming"
print(len(msg))
print(msg.endswith("ing"))
print(msg.startswith("py"))
print(msg.capitalize())
print(msg.lower())
print(msg.upper())
print(msg.title())
print(msg.find("pro"))
print(msg.count("p"))
print(msg.replace("python", "java"))

# Escape sequences
print("Hello\nWorld")
print("Name\tAge")
print("He said, \"Hi\"")
print("C:\\Users\\Python")