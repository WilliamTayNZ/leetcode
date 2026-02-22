from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_length = 0


        for num in nums_set:
            if (num - 1) not in nums_set:
                current_length = 1
                next_num = num + 1
                while next_num in nums_set:
                    current_length += 1
                    next_num += 1
                longest_length = max(current_length, longest_length)

        return longest_length

# O(n) time complexity
# O(n) space complexity (storing the numbers in a set)

solution = Solution()
print(solution.longestConsecutive([100,4,200,1,3,2]))
print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(solution.longestConsecutive([1,0,1,2]))