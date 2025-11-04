class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0

        for right in range(len(prices)):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)
            else:
                left = right

        return max_profit
