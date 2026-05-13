class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = set(nums)
        length = 0
        for num in ans:
            if (num - 1) not in ans:
                longest = 1
                while num + longest in ans:
                    longest += 1
                length = max(length, longest)
        return length