class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        maxLen = 0
        l = 0
        
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            maxLen = max(r - l + 1, maxLen)
        return maxLen