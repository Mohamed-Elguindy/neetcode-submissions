# Data Structures – Quick Notes

## 1. Dictionary (Hash Map)

- Stores data as **key-value pairs**.
- Allows fast lookup using keys.
- Python implementation: `dict`.
- Java implementation: `HashMap`.
- Average lookup, insertion, and deletion: **O(1)**.
- Common use cases: counting frequencies, caching, Two Sum, and fast lookups.

```python
d = {}
d["apple"] = 3

if "apple" in d:
    print(d["apple"])
```

## 2. Hash Table

- A data structure that implements key-value storage.
- Uses a **hash function** to convert keys into hash values, determining where data is stored.
- Collisions occur when different keys map to the same location.
- Average lookup: **O(1)**.
- Used in dictionaries, HashMaps, and caches.

## 3. B-Tree

- A self-balancing search tree.
- Each node can contain multiple sorted keys and multiple children.
- Keeps data sorted and supports efficient searching, insertion, and deletion.
- Search: **O(log n)**.
- Designed to reduce disk I/O by storing multiple keys per node.

## 4. B+ Tree

- A variation of the B-Tree, commonly used in database indexing.
- Internal nodes store keys for navigation.
- Actual records or record pointers are stored in leaf nodes.
- Leaf nodes are linked, allowing efficient sequential traversal.
- Search: **O(log n)**.
- Excellent for exact lookups, range queries, and ordered traversal.

## Quick Comparison

| Structure  | Main Advantage                   | Common Use           |
| ---------- | -------------------------------- | -------------------- |
| Hash Table | Fast exact lookup                | Dictionaries, caches |
| B-Tree     | Ordered searching                | Storage systems      |
| B+ Tree    | Ordered indexing + range queries | Database indexes     |

**Key Takeaway:**

- Hash Table → Fast key lookup.
- B-Tree → Balanced, ordered search.
- B+ Tree → Database indexing, exact lookups, and efficient range queries.
