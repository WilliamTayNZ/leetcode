# How many ways to climb 1 step?
# 1

# How many ways to climb 2 steps?
# 2 (1+1, or 2)

# How many ways to climb 3 steps?
# 2 steps: 2 (+ 1 step)
# 1 step: 1 (+ 2 steps)

# How many ways to climb 4 steps?
# 3 steps: 3 (+ 1 step)
# 2 steps: 2 (+ 2 steps)

# How many ways to climb 5 steps?
# 4 steps: 5 (+ 1 step)
# 3 steps: 3 (+ 2 steps)

# From the bottom-up approach, we can see the pattern


# Bottom-up DP, O(n) time and space
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2

        dp = [0] * (n+1)

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]


# O(n) time, O(1) space by only storing the previous 2 at all times
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2

        prev, curr = 1, 2

        for i in range(3, n+1):
            prev, curr = curr, prev + curr
        
        return curr