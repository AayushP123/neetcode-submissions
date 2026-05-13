class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profMax = 0
        minPrice = prices[0]

        for num in prices:
            profMax = max(profMax, num - minPrice)
            minPrice = min(minPrice, num)
        return profMax
