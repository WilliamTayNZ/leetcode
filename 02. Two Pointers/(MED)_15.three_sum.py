# Always make sure of no errors before running
# We know len(nums) >= 3

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        triplet_array = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: # Avoid duplicate
                continue

            left = i+1
            right = len(nums) - 1

            target = 0 - nums[i]

            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    triplet_array.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1

        return triplet_array

        # Think about why it cannot be solved in less than O(n^2)
        # Don't care about whether you can find O(n), just solve yourself first
        # ALso think about whether the problem is actually possible to solve in O(n)