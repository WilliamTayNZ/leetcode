class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        max_left = height[left]
        max_right = height[right]

        total_water = 0

        while left < right:
            if max_left > max_right:
                right -= 1
                max_right = max(max_right, height[right])
                total_water += max_right - height[right]
            else:
                left += 1
                max_left = max(max_left, height[left])
                total_water += max_left - height[left]
        
        return total_water

# November 10th 2025
# Mindblown, genuinely beautiful problem