class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        profit = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = max(profit, prices[r] - prices[l])
            elif prices[l] > prices[r]:
                l = r
            r += 1
        return profit
            