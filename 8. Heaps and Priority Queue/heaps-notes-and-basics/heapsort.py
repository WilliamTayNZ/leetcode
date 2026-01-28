def max_heapify(arr, heap_size, i):
    # Children for 0-based indexing
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i

    if l < heap_size and arr[l] > arr[largest]:
        largest = l

    if r < heap_size and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, heap_size, largest)

def build_max_heap(arr):
    n = len(arr)

    # The last non-leaf node is at index (n // 2) - 1
    # All nodes after this are leaves and hence heaps by definition
    # We have to check all non-leaves to see if they follow the heap property

    # We go backwards to the root
    for i in range((n // 2) - 1, -1, -1):
        max_heapify(arr, n, i)

def heapsort(arr): # O(n log n) time, O(1) space because sorts in-place
    n = len(arr)
    build_max_heap(arr)

    # We repeatedly extract the largest element, and swap it with the end of the unsorted part of the array
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0] 
        max_heapify(arr, i, 0)

def main():
    arr = [54, 12, 89, 3, 22, 1, 90, 45, 7, 33, 67, 8, 15, 4, 11, 100, 2, 9, 55, 18, 29, 6, 72, 41, 0, -5, 14, 21, 99, 31]

    heapsort(arr)
    print(f"Sorted array: {arr}")

main()