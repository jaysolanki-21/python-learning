# Chapter 5: Dictionary & Sets

---

## 1. Dictionary

### Properties
- **Unordered**: Items do not maintain insertion order (before Python 3.7, now it preserves order but conceptually unordered).
- **Mutable**: Can be changed after creation.
- **Indexed**: Access items using keys.
- **Cannot contain duplicate keys**: If the same key is assigned a new value, the old value is overwritten.

---

### Functions / Methods

- `.items()` — Returns a view object containing `(key, value)` pairs.
  ```python
  a = {"name": "Jay", "age": 21}
  print(a.items())  # dict_items([('name', 'Jay'), ('age', 21)])
  ```
- `.keys()` — Returns all keys.
  ```python
  print(a.keys())  # dict_keys(['name', 'age'])
  ```
- `.update({})` — Updates dictionary with given key–value pairs.
  If key exists, value is updated. If key not found, new key–value is added.
  ```python
  a.update({"age": 22, "city": "Ahmedabad"})
  print(a)  # {'name': 'Jay', 'age': 22, 'city': 'Ahmedabad'}
  ```
- `.get(key)` — Returns value of key. Returns None if key not found (safe).
  ```python
  print(a.get("name"))    # Jay
  print(a.get("salary")) # None
  ```
- `a[key]` — Access value directly. Raises KeyError if key not found.
  ```python
  print(a["name"])  # Jay
  ```
- `.pop(key)` — Removes the element with specified key.
  ```python
  a.pop("age")
  print(a)  # {'name': 'Jay', 'city': 'Ahmedabad'}
  ```
- `.popitem()` — Removes the last inserted key–value pair.
  ```python
  a.popitem()
  print(a)  # {'name': 'Jay'}
  ```

## 2. Sets

### Properties
- **Unordered**: Items have no defined order.
- **Unindexed**: Cannot access elements using index.
- **No duplicate values**: Only unique items are stored.

### Methods
- `.add(value)` — Adds element to set.
  ```python
  s = {1, 2, 3}
  s.add(4)
  print(s)  # {1, 2, 3, 4}
  ```
- `.clear()` — Removes all elements.
  ```python
  s.clear()
  print(s)  # set()
  ```
- `len(s)` — Returns number of elements.
  ```python
  print(len({1, 2, 3}))  # 3
  ```
- `.remove(value)` — Removes specified element. Raises KeyError if not found.
  ```python
  s = {1, 2, 3}
  s.remove(2)
  print(s)  # {1, 3}
  ```
- `.pop()` — Removes a random element.
  ```python
  s = {5, 6, 7}
  s.pop()
  print(s)
  ```
- `.union(set2)` — Returns union of sets.
  ```python
  s1 = {1, 2, 3}
  s2 = {3, 4, 5}
  print(s1.union(s2))  # {1, 2, 3, 4, 5}
  ```
- `.intersection(set2)` — Returns common elements.
  ```python
  print(s1.intersection(s2))  # {3}
  ```
- `.copy()` — Returns a shallow copy of set.
  ```python
  s3 = s1.copy()
  print(s3)  # {1, 2, 3}
  ```
