
# Chapter 4: List & Tuple

## 1. List

- **Definition**: A list is an ordered, mutable (changeable) collection in Python.
- **Syntax**:
  ```python
  my_list = [1, 2, 3, 4, 5]
  ```

- **Accessing Values**
  By indexing (0-based):
  ```python
  print(my_list[0])   # First element
  print(my_list[-1])  # Last element
  ```

- **Mutable Property**
  Lists can be modified:
  ```python
  my_list[2] = 100
  print(my_list)  # [1, 2, 100, 4, 5]
  ```

- **Slicing & Indexing**
  Get parts of a list:
  ```python
  print(my_list[1:4])   # Elements at index 1 to 3
  print(my_list[:3])    # First three elements
  print(my_list[::2])   # Step slicing
  ```

- **Common List Methods**
  - `append()` — Add an element at the end.
    ```python
    my_list.append(6)
    ```
  - `sort()` — Sort elements in ascending order.
    ```python
    nums = [3, 1, 4]
    nums.sort()
    ```
  - `reverse()` — Reverse the list order.
    ```python
    nums.reverse()
    ```
  - `insert(index, value)` — Insert at a specific position.
    ```python
    my_list.insert(2, 50)
    ```
  - `pop(index)` — Remove element at index (default last).
    ```python
    my_list.pop()
    my_list.pop(1)
    ```
  - `remove(value)` — Remove first occurrence of a value.
    ```python
    my_list.remove(50)
    ```

## 2. Tuple

- **Definition**: A tuple is an ordered, immutable collection.
- **Syntax**:
  ```python
  my_tuple = (10, 20, 30)
  ```

- **Immutable Property**
  Tuples cannot be modified:
  ```python
  my_tuple[1] = 50   # ❌ Error
  ```

- **Methods**
  - `count(value)` — Counts occurrences.
    ```python
    my_tuple.count(10)
    ```
  - `index(value)` — Finds index of first occurrence.
    ```python
    my_tuple.index(20)
    ```
  - Membership (`in`):
    ```python
    30 in my_tuple   # True
    ```
  - `len()`:
    ```python
    len(my_tuple)   # 3
    ```
  - Slicing:
    ```python
    print(my_tuple[0:2])   # (10, 20)
    ```

## Key Differences: List vs Tuple

| Feature   | List   | Tuple  |
|-----------|--------|--------|
| Syntax    | [ ]    | ( )    |
| Mutable   | ✅ Yes | ❌ No  |
| Methods   | Many   | Limited|
| Use Case  | Dynamic data | Fixed data |