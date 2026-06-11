class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return false

        se = {}
        te = {}

        for i in range(len(s)):
            se[s[i]] = 1 + se.get(s[i], 0)
            te[t[i]] = 1 + te.get(t[i], 0)
        return se == te