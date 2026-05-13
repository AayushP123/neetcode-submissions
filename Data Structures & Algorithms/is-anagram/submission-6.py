class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        se = {}
        te = {}

        for i in range(len(s)):
            se[s[i]] = se.get(s[i], 0) + 1
            te[t[i]] = te.get(t[i], 0) + 1
        return se == te