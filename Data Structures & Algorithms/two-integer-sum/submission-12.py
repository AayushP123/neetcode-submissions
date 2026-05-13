class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in ans:
                return[ans[diff], i]
            ans[n] = i
            