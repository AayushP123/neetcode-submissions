class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxVal = 0
        minPrice = prices[0]

        for val in prices:
            maxVal = max(maxVal, val - minPrice)
            minPrice = min(minPrice, val)
        return maxVal