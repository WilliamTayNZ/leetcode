class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # We want to reach the top, which we can think of as index n, or the n+1'th step
        # Start at 0 or 1 

        # Pay the cost of the step, then take 1 or 2 steps

        # dp array stores min cost to reach each step

        # 2 <= cost.length <= 1000

        n = len(cost)

        dp = [0] * (n+1) # n+1 is the top. cost remains 0 at both index 0 and 1

        for i in range(2, n+1):
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])

        return dp[n]
    
# With O(1) space
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        prev, curr = 0, 0

        for i in range(2, n+1):
            prev, curr = curr, min(prev + cost[i-2], curr + cost[i-1])

        return curr