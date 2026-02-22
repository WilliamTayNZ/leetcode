class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, window_size = 0,1

        max_profit = 0

        for right in range(window_size, len(prices)):
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
            if prices[right] < prices[left]:
                left = right

        return max_profit

# November 11th, 2025