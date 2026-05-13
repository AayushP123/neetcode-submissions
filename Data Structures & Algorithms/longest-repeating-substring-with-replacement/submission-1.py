class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        check = {}
        l = 0
        ans = 0
        maxC = 0

        for r in range(len(s)):
            check[s[r]] = 1 + check.get(s[r], 0)
            maxC = max(maxC, check[s[r]])

            while (r - l + 1) - maxC > k:
                check[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans