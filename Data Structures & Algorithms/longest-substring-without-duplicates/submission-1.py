class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        valCheck = {}
        l, r = 0, 0

        for i in range(len(s)):
            if s[i] in valCheck:
                l = max(valCheck[s[i]] + 1, l)
            valCheck[s[i]] = i
            r = max(r, i - l + 1)
        return r