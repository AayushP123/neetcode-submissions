class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Come from both sides, l, r
        # If theres a mismatch, check if moving l + 1 would work, or r-1
        # Else, return False
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                checkLeft = s[l + 1: r + 1]
                checkRight = s[l : r]
                return checkLeft == checkLeft[::-1] or checkRight == checkRight[::-1]
            l = l + 1
            r = r - 1
        return True