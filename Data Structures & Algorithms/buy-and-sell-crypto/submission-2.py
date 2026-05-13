class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxVal = 0
        minVal = prices[0]

        for val in prices:
            maxVal = max(maxVal, val - minVal)
            minVal = min(minVal, val)
        return maxVal