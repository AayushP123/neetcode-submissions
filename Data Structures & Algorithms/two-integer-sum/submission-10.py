class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        test = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in test:
                return[test[diff], i]
            test[n] = i