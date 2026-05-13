class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = set(nums)
        maxval = 0

        for num in ans:
            if (num - 1) not in ans:
                length = 1
                while (num + length) in ans:
                    length += 1
                maxval = max(length, maxval)
        return maxval