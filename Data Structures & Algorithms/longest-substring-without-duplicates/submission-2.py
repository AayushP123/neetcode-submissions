class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charVal = {} # Character --> Index
        l = 0
        maxRes = 0

        for r in range(len(s)):
            if s[r] in charVal:
                l = max(charVal[s[r]] + 1, l)
            charVal[s[r]] = r
            maxRes = max(maxRes, r - l + 1)
        return maxRes