class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # Key intuition: at each step, at least 1 half will be sorted.

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Else, check if left half is sorted
            elif nums[left] <= nums[mid]:
                if nums[mid] < target or target < nums[left]: # check if target is too big or too small for this range
                    left = mid + 1
                else:
                    right = mid - 1

            # Else, right is definitely sorted i.e nums[mid] <= nums[right]
            else:
                if nums[mid] > target or target > nums[right]: # check if target is too big or too small for this range
                    right = mid - 1
                else:
                    left = mid + 1
            
        return -1

# December 26th, 2025