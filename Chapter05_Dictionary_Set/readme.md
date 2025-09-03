# Chapter 5: Dictionary & Sets (Quick Reference)

## Dictionary
- **Properties**
  - Unordered, Mutable, Indexed
  - No duplicate keys allowed

- **Functions**
  - `a.items()` → all key–value pairs
  - `a.keys()` → all keys
  - `a.update({})` → add/update items
  - `a.get(key)` → safe access
  - `a[key]` → direct access (KeyError if missing)
  - `a.pop(key)` → remove key
  - `a.popitem()` → remove last inserted item

---

## Set
- **Properties**
  - Unordered, Unindexed
  - No duplicate values

- **Methods**
  - `s.add(x)`
  - `s.clear()`
  - `len(s)`
  - `s.remove(x)`
  - `s.pop()`
  - `s.union(set2)`
  - `s.intersection(set2)`
  - `s.copy()`
