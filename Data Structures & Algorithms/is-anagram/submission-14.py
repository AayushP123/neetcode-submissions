class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sq = {} # character -> amount of chars
        tq = {}

        for i in range(len(s)):
            sq[s[i]] = 1 + sq.get(s[i], 0);
            tq[t[i]] = 1 + tq.get(t[i], 0);
        return sq == tq