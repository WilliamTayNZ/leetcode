## Quickselect

https://www.youtube.com/watch?v=wiNfjkMDl3AWx

Quickselect = selection via pivot

**Goal:**
Find the **k-th smallest (or largest)** element without fully sorting the array.

**Key idea:**  
Use the same partitioning logic as Quicksort, but recurse into **only one side**.

---

### Core Insight

After partitioning around a pivot:

* 1. The pivot is in its final sorted position
* 2. We can determine the rank of the pivot
* 3. Only one side can possibly contain the k-th element

So unlike Quicksort:
**We discard half the array each step.**

---

### Partitioning (same as Quicksort)

* 1. Choose a pivot (often random or median-of-three)
* 2. Partition the array so:
  * Elements `< pivot` are on the left
  * Elements `> pivot` are on the right
* 3. Pivot ends up in its correct sorted index `p`

---

### Selection Logic

Let `p` = index of pivot after partitioning

* If `p == k` → done (found k-th smallest)
* If `k < p` → recurse left
* If `k > p` → recurse right

Only **one recursive call**, never both.

---

### Pivot Choice

Pivot quality affects performance.

Common choices:
* Random pivot
* Median-of-three

Balanced pivots → fewer steps.

---

### Time Complexity

* Average case: **O(n)**
* Worst case: **O(n²)**

---

### Space Complexity

* O(1) extra space (in-place)
* O(log n) recursion stack on average  
  (O(n) worst case)

---

### Relationship to Quicksort

| Quicksort | Quickselect |
|----------|-------------|
| Fully sorts array | Finds one element |
| Recurse on both sides | Recurse on one side |
| Average O(n log n) | Average O(n) |

---

### When to Use Quickselect

Use Quickselect when:
* You only need the k-th smallest / largest
* Median, percentile, or threshold problems
* Full sorting is unnecessary
