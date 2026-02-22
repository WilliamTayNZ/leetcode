from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[nums[i]] = i


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([3,2,4], 6))
    print(solution.twoSum([3,3], 6))
