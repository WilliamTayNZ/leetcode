class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        left, right = 0, n-1

        if nums[left] <= nums[right]: # handles edge case where n = 1
            return nums[left]
        
        else:
            minimum = nums[left]

            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] < minimum: 
                    minimum = nums[mid]
                    right = mid - 1
                else: 
                    left = mid + 1

        
        return minimum

# December 25th, 2025