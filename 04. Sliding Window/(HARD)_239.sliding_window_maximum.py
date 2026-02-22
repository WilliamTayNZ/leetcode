from collections import deque

class Solution: 
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()

        # Initial window
        for i in range(k):
            while len(dq) > 0 and dq[-1] < nums[i]:
                dq.pop()
            dq.append(nums[i])

        max_array = [dq[0]]
        
        # Start moving window
        l = 1
        r = k

        while r < len(nums): 
            if nums[l-1] == dq[0]:
                dq.popleft()

            while len(dq) > 0 and dq[-1] < nums[r]: 
                dq.pop()
            dq.append(nums[r])

            max_array.append(dq[0])
            l += 1
            r += 1

        return max_array

# November 19, 2025
# Key takeaway: we use double-ended queue since we have to pop from both sides
# When review, solve it with index and not value
