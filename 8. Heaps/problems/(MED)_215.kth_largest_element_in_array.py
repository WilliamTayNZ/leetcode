import heapq

class MaxHeapSolution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 1. Max-heapify array in O(n) time
        heapq.heapify_max(nums)

        # 2. Pop from heap k times and return that 
        for i in range(k):
            popped = heapq.heappop_max(nums)

        return popped
    
# O(N + K log n) time, O(1) space