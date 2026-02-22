import heapq

class MedianFinder:

    def __init__(self):
        self.lower_half = [] # max-heap
        self.upper_half = [] # min-heap

    def addNum(self, num: int) -> None: # O(log n)
        # 1. Figure out which heap to add the element to

        if not self.lower_half and not self.upper_half:
            heapq.heappush_max(self.lower_half, num)
        elif num < self.lower_half[0]:
            heapq.heappush_max(self.lower_half, num)
        else:
            heapq.heappush(self.upper_half, num)

        # 2. Make sure the heaps are balanced

        # If lower half's length is now greater than 1 more than upper half
        if len(self.lower_half) - len(self.upper_half) > 1:
            moved = heapq.heappop_max(self.lower_half)
            heapq.heappush(self.upper_half, moved)
        # Else if lower half's length is now greater than 1 less than upper half
        elif len(self.lower_half) - len(self.upper_half) < -1:
            moved = heapq.heappop(self.upper_half)
            heapq.heappush_max(self.lower_half, moved)


    def findMedian(self) -> float: # O(1)
        if len(self.lower_half) == len(self.upper_half):
            return (self.lower_half[0] + self.upper_half[0]) / 2
        elif len(self.lower_half) > len(self.upper_half):
            return self.lower_half[0]
        else:
            return self.upper_half[0]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()