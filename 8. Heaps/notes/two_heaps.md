# Two Heaps Algorithm

## The algorithm

1. Divide your data into 2 parts.
2. Store the smaller half in a max-heap.
3. Store the larger half in a min-heap.
4. Balance the heaps to maintain equal (or nearly equal) sizes.

## Median algorithm

Imagine you're a teacher keeping track of student scores as they come in. You want to know the median score at any given time. Here's how the Two Heaps technique would work...

1. Set up two heaps:

- Max heap for the lower half of scores
- Min heap for the upper half of scores

2. For each score that comes in:

- If it's lower than the top of the max heap, add it to the max heap
- Else, add it to the min heap

3. Balance the heaps:

- If one heap has at least 2 elements more than the other, move its top element to the other heap

4. Find the median:

- If the heaps have equal size, the median is the average of their top elements
- If not, the median is the top element of the larger heap.

## When to use it

This technique is particularly useful when:

- You need to divide a dataset into two parts
- You frequently need to find the smallest element from one part and the largest from the other
- You're dealing with problems involving medians, scheduling, or data stream processing.
