class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxChar = 0
        maxAns = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxChar = max(maxChar, count[s[r]])

            while(r - l + 1) - maxChar > k:
                count[s[l]] -= 1
                l += 1
            maxAns = max(maxAns, r - l + 1)
        return maxAns