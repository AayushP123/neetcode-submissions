class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ithDay = prices[0]
        maxProfit = 0

        for i in prices:
            maxProfit = max(maxProfit, i - ithDay)
            ithDay = min(ithDay, i)
        return maxProfit