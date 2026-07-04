class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.moneyMax(nums[1:]),
                    self.moneyMax(nums[:-1]))

    def moneyMax(self, nums: List[int]) -> int:
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            ans = [0] * len(nums)
            ans[0] = nums[0]
            ans[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                ans[i] = max(ans[i - 1], nums[i] + ans[i - 2])
            return ans[-1]