class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sp = {}
        tp = {}
        for i in range(len(s)):
            sp[s[i]] = 1 + sp.get(s[i], 0)
            tp[t[i]] = 1 + tp.get(t[i], 0)
        return sp == tp