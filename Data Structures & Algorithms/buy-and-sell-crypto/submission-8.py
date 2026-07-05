class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minVal = prices[0]
        maxVal = 0
        for num in prices:
            minVal = min(minVal, num)
            maxVal = max(maxVal, num - minVal)
        return maxVal