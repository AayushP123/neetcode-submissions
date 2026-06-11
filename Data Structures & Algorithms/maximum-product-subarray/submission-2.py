class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        curMax, curMin = 1, 1

        for num in nums:
            temp = curMax * num
            curMax = max(curMax * num, num, curMin * num)
            curMin = min(temp, num, curMin * num)
            ans = max(ans, curMax)
        return ans