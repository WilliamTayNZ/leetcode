# Heaps

A **Heap** is a specialized tree-based data structure that satisfies the **Heap Property**. It is the most efficient way to handle "Priority Queue" problems where you need constant access to the minimum or maximum element.

---

## 1. Core Concepts

### The Heap Property
* **Min-Heap:** Parent node $\le$ Child nodes. The smallest element is always at the root.
* **Max-Heap:** Parent node $\ge$ Child nodes. The largest element is always at the root.



### Array Mapping (0-Indexed)
Python’s `heapq` uses **0-based indexing**. For an element at index $i$:
* **Root:** Always `heap[0]`
* **Left Child:** $2i + 1$
* **Right Child:** $2i + 2$
* **Parent:** $(i - 1) \space // \space 2$

> **Note:** While some textbooks use 1-based indexing ($2i$ and $2i+1$), standard library implementations (like Python's) use 0-based indexing to align with how arrays work in memory.

---

## 2. Complexity Analysis

| Operation | Time Complexity | Note |
| :--- | :--- | :--- |
| **Push** | $O(\log n)$ | Sift-up |
| **Pop** | $O(\log n)$ | Sift-down |
| **Peek** | $O(1)$ | Access `heap[0]` |
| **Heapify** | $O(n)$ | Linear time in-place transformation |

---

## 3. Python Implementations

### A. The Standard (Min-Heap)
Python’s `heapq` module defaults to a Min-Heap.

```python
import heapq

data = [10, 2, 15, 6]
heapq.heapify(data)         # Returns None, transforms list to heap in-place: O(n)
heapq.heappush(data, 4)     # Add element: O(log n)
smallest = heapq.heappop(data) # Remove and return root: O(log n)
```

### B. The Classic Workaround (Max-Heap via Negation)

For versions of Python prior to 3.14, or when working in older environments, we simulate a Max-Heap by multiplying values by $-1$.

```python
max_heap = []
nums = [10, 20, 5]

for n in nums:
    heapq.heappush(max_heap, -n)

# Pop returns -20, so we negate it back to 20
largest = -heapq.heappop(max_heap)
```

### C. The New Standard (Python 3.14 Native Max-Heap)

As of Python 3.14, the `heapq` module includes native support for max-heaps, removing the need for the negation hack.

```python
import heapq

data = [1, 5, 2, 8]

# Native max-heap functions
heapq.heapify_max(data)
heapq.heappush_max(data, 10)
largest = heapq.heappop_max(data) # Returns 10
```

## 4. Key Use Cases

- Repeatedly extract the smallest/largest item
- Maintaining a top-k or bottom-k set of values
- Real time ranking, greedy selection, etc.
- Need to sort on the fly, faster than O(n log n)

(update)

## 5. Pro-Tips for Interviews

* **Priority Tuples**: If sorting objects, store them as `(priority, value)` tuples. The heap will sort by priority first.
  * For example, if you need counts, you can use Counter() and easily push tuples with this.

* **Heapify is faster**: If you have all your data upfront, use heapify() ($O(n)$) instead of calling heappush() $n$ times ($O(n \log n)$).

* **Search:** Do not use a heap if you need to search for an element. It takes $O(n)$, making it no better than a standard list.