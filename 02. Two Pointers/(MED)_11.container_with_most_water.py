class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        max_area = 0

        while left < right:
            area = (right - left) * min(height[left], height[right])

            if area > max_area:
                max_area = area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# Solved 10th November 2025
# Intuition: We start with the widest container since pointers are at both ends, hence to find a greater area, at each iteration we move whichever pointer has the lower height.