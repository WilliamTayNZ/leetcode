# In this file: my original solution, and optimal solution
# Note: division operation not allowed, and would cause division by zero error anyway

from typing import List

# Optimal O(n) time and O(1) space solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)

        prefix_product = 1

        for i in range(len(nums)):
            answer[i] = prefix_product 
            prefix_product *= nums[i]

        suffix_product = 1

        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= suffix_product
            suffix_product *= nums[i]

        return answer
    

# My original O(n) time and O(n) space solution, using redundant hashmap
class WorseSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        hashmap = {}
        n = len(nums)
        prefix_product = 1

        for i in range(n):
            hashmap[i] = prefix_product
            prefix_product *= nums[i]

        suffix_product = 1

        for i in range(n - 1, -1, -1):
            hashmap[i] *= suffix_product
            suffix_product *= nums[i]

        answer = [0] * n

        for i in range(n):
            answer[i] = hashmap[i]

        return answer
    
    
solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))
print(solution.productExceptSelf([-1,1,0,-3,3]))
    
worseSolution = WorseSolution()
print(worseSolution.productExceptSelf([1,2,3,4]))
print(worseSolution.productExceptSelf([-1,1,0,-3,3]))

