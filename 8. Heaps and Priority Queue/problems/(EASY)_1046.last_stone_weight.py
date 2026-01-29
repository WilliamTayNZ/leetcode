import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # We want the greatest 2 elements at each turn
        # There are 1-30 elements. We use a max-heap.

        max_heap = [-stone for stone in stones] # O(n)
        heapq.heapify(max_heap)

        while len(max_heap) > 1: 
            y = -heapq.heappop(max_heap) # y is greater
            x = -heapq.heappop(max_heap)

            if x != y:
                heapq.heappush(max_heap, -(y-x))

        if max_heap:
            return -max_heap[0]
        else:
            return 0