class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ansList = set(nums)
        curMax = 0

        for n in ansList:
            count = 1
            while (n + count) in ansList:
                count += 1
            curMax = max(curMax, count)
        return curMax