# Hashing & Frequency Patterns

Core techniques for fast lookups, duplicate detection, and frequency counting.

## 1. Hash Map (Python Dictionary)

- Stores data as **key-value pairs**.
- Uses a hash function to locate keys efficiently.
- Average lookup, insertion, and deletion: **O(1)**.
- Useful when you need to associate values with additional information, such as indices or frequencies.

```python
d = {}
d["apple"] = 3

if "apple" in d:
    print(d["apple"])
```

## 2. Hash Set

- Stores unique elements without associated values.
- Useful for checking whether an element already exists.
- Average lookup, insertion, and deletion: **O(1)**.

```python
s = set()
s.add(5)

if 5 in s:
    print("Found")
```

## 3. Frequency Counting (Counter)

- `collections.Counter` is a specialized dictionary for counting occurrences.
- Useful for comparing frequencies and detecting anagrams.

```python
from collections import Counter

freq = Counter("hello")
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

## Problem Patterns

### Two Sum — Complement Lookup

**Technique:** Hash Map

- Calculate the complement: `target - current_number`.
- Check whether the complement exists in the dictionary.
- If found, return both indices.
- Otherwise, store the current number and its index.

**Complexity:** O(n) time, O(n) space.

### Valid Anagram — Frequency Counting

**Technique:** Hash Map / Counter

- Check whether both strings have equal lengths.
- Count character frequencies.
- Compare the frequencies or increment one count and decrement the other.
- If all counts are zero, the strings are anagrams.

**Complexity:** O(n) time, O(k) space, where k is the number of distinct characters.

### Contains Duplicate — Set Lookup

**Technique:** Hash Set

- Iterate through the array.
- Check whether the current element already exists in the set.
- If it exists, a duplicate is found.
- Otherwise, add it to the set.

**Complexity:** O(n) time, O(n) space.

## Quick Reference

| Problem | Technique | Main Idea |
|---|---|---|
| Two Sum | Hash Map | Complement lookup |
| Valid Anagram | Counter / Hash Map | Frequency counting |
| Contains Duplicate | Hash Set | Membership checking |

## Key Takeaways

- **Dictionary:** Store relationships between keys and values.
- **Set:** Track unique elements and check membership.
- **Counter:** Count occurrences efficiently.
- **Hashing:** Avoid repeated linear searches using efficient lookups.
- Average hash-based lookup: O(1).