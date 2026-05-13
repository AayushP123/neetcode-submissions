class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charVal = {}
        l = 0
        maxRes = 0

        for r in range(len(s)):
            if s[r] in charVal:
                l = max(l, charVal[s[r]] + 1)
            charVal[s[r]] = r
            maxRes = max(maxRes, r - l + 1)
        return maxRes