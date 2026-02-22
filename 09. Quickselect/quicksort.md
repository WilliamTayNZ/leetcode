## Quicksort

Quicksort = Pivot

The pivot meets the following 3 conditions after we sort it:

* 1. Pivot is in correct position in final, sorted array. 
* 2. This means all items to the left are smaller
* 3. And all items to the right are larger


### Partitioning
* 1. (Optional) Move the pivot to the end of the array for convenience
* 2. Look for 2 items: (the first) itemFromLeft that is larger than pivot, (the first) itemFromRight that is smaller than pivot
* 3. Swap itemFromLeft and itemFromRight
* 4. Repeat until index of itemFromLeft > index of itemFromRight
* 5. Swap itemFromLeft with pivot. Now our pivot is in its correct spot.
* 6. Repeat whole process (partition) recursively on each side of pivot.


How to choose the pivot?
We want a pivot that divides the array in half to spread the work as evenly as possible.
One way to attempt this is the median-of-three. Take the first, last, and middle element of the array and take the median of those 3 as our pivot.

Worst case: $O(n^2)$ <br/>
Average case: $O(n log n)$
