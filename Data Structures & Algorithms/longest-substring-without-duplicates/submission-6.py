class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        l = 0
        check = {}

        for r in range(len(s)):
            if s[r] in check:
                l = max(check[s[r]] + 1, l)
            check[s[r]] = r
            maxLen = max(maxLen, r - l + 1)
        return maxLen