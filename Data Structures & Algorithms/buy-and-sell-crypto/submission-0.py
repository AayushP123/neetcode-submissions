class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxest = 0
        dayVal = prices[0]

        for i in prices:
            maxest = max(maxest, i - dayVal)
            dayVal = min(dayVal, i)
        return maxest