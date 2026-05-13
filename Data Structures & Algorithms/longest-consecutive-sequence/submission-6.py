class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = set(nums)
        longest = 0

        for num in ans:
            if (num - 1) not in ans:
                out = 1
                while (num + out) in ans:
                    out += 1
                longest = max(out, longest)
        return longest