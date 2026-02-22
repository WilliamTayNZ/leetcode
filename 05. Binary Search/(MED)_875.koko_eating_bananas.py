import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = math.ceil(sum(piles) / h) # we can start here because logically, this is the minimum possible value of k
        right = max(piles) # O(n)

        while left <= right:
            mid = (left + right) // 2

            hours_needed = 0
            for i in range(len(piles)):
                hours_needed += math.ceil(piles[i] / mid)
            
            if hours_needed <= h:
                k = mid
                right = mid - 1 # search for smaller values of k
            else:
                left = mid + 1

        return k

# December 25th, 2025 (Merry Christmas!)