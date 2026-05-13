class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currMax = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            currMax = max(currMax, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return currMax