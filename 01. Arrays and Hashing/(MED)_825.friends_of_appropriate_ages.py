import collections
from typing import List

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def requestTrue(a, b):
            if (b <= 0.5 * a + 7) or (b > a):
                return False
            return True

        age_counter = collections.Counter(ages)
        total = 0

        for a, a_count in age_counter.items():
            for b, b_count in age_counter.items():
                if requestTrue(a, b):
                    total += a_count * b_count
                    if a == b:
                        total -= a_count

        return total

solution = Solution()
print(solution.numFriendRequests(ages = [16,16]))
print(solution.numFriendRequests(ages = [16,17,18]))
print(solution.numFriendRequests(ages = [20,30,100,110,120]))