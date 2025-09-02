# Chapter 4: List & Tuple Examples

# ----- List -----
print("=== List Examples ===")
my_list = [10, 20, 30, 40]

# Access
print(my_list[0])   # 10
print(my_list[-1])  # 40

# Mutability
my_list[1] = 200
print(my_list)      # [10, 200, 30, 40]

# Slicing
print(my_list[1:3])  # [200, 30]
print(my_list[::-1]) # [40, 30, 200, 10]

# Methods
my_list.append(50)
print(my_list)       # [10, 200, 30, 40, 50]

nums = [3, 1, 4, 2]
nums.sort()
print(nums)          # [1, 2, 3, 4]

nums.reverse()
print(nums)          # [4, 3, 2, 1]

my_list.insert(2, 99)
print(my_list)       # [10, 200, 99, 30, 40, 50]

my_list.pop()
print(my_list)       # [10, 200, 99, 30, 40]

my_list.remove(99)
print(my_list)       # [10, 200, 30, 40]

# ----- Tuple -----
print("\n=== Tuple Examples ===")
my_tuple = (5, 10, 15, 10)

print(my_tuple[0])       # 5
print(my_tuple[1:3])     # (10, 15)

print(my_tuple.count(10)) # 2
print(my_tuple.index(15)) # 2

print(10 in my_tuple)    # True
print(len(my_tuple))     # 4
