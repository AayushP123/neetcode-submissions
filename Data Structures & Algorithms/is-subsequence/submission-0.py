class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Can't move position of chars, s has to be in t
        # Start pointer at beginning of both words
        # Move each when it matches, else move t pointer
        # Keep moving until end of s or t, return true if no 
        # Errors occur
        i = 0
        j = 0
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                i += 1
                j += 1
            else:
                i += 1
        return j == len(s)