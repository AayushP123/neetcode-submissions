class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        curr = ""
        dp = [[False] * n for _ in range(n)]

        for l in range(n - 1, -1, -1):
            for r in range(l, n):
                if s[l] == s[r]:
                    if r - l <= 2 or dp[l + 1][r - 1]:
                        dp[l][r] = True
                        ans += 1
        return ans