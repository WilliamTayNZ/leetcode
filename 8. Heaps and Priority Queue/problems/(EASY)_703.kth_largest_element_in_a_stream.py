import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k

        self.top_k_elements = nums
        heapq.heapify(self.top_k_elements) # O(n)

        # The heap is initialised as a min-heap with the k greatest elements

        # Edge case
        if k == len(nums) + 1:
            heapq.heappush(self.top_k_elements, -float(inf))
        else:
            # Remove elements until the top k are left
            for i in range(len(nums) - k): # O(n log k)
                heapq.heappop(self.top_k_elements)


    def add(self, val: int) -> int:
        heapq.heappush(self.top_k_elements, val)
        heapq.heappop(self.top_k_elements)

        return self.top_k_elements[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)