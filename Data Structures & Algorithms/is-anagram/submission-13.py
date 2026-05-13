class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        keys = {}
        keyt = {}

        for i in range(len(s)):
            keys[s[i]] = 1 + keys.get(s[i], 0)
            keyt[t[i]] = 1 + keyt.get(t[i], 0)
        return keys == keyt