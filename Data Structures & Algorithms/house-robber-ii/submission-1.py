class Solution:
    def rob(self, nums: List[int]) -> int:
         return max(nums[0], self.robber(nums[1:]), self.robber(nums[:-1]))

    def robber(self, nums):
        prev, curr = 0, 0

        for n in nums:
            temp = max(n + prev, curr)
            prev = curr
            curr = temp
        return curr