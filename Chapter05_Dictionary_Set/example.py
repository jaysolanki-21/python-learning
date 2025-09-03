# Chapter 5: Dictionary & Sets Example

# ----------------- Dictionary -----------------
print("=== Dictionary Example ===")
a = {"name": "Jay", "age": 21}

# items, keys
print(a.items())
print(a.keys())

# update
a.update({"city": "Ahmedabad"})
print(a)

# get vs direct access
print(a.get("name"))   # Jay
# print(a["salary"])   # would raise KeyError

# pop, popitem
a.pop("age")
print(a)
a.popitem()
print(a)

# ----------------- Set -----------------
print("\n=== Set Example ===")
s1 = {1, 2, 3}
s2 = {3, 4, 5}

# add
s1.add(10)
print(s1)

# remove
s1.remove(2)
print(s1)

# union, intersection
print(s1.union(s2))
print(s1.intersection(s2))

# copy
s3 = s1.copy()
print(s3)
