class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = set(nums)
        maxCons = 0

        for n in ans:
            if not (n - 1) in ans:
                length = 1
                while (n + length) in ans:
                    length += 1
                maxCons = max(length, maxCons)
        return maxCons