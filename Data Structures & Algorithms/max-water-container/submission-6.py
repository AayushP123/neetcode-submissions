class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Create max variable, which constantly updates per two pointer update
        l = 0
        r = len(heights) - 1
        curArea = 0

        while l < r:
            area = (min(heights[l], heights[r]))*(r - l)
            curArea = max(area, curArea)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return curArea