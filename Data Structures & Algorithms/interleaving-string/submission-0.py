class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for row in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True
        
        for row in range(len(s1), - 1, -1):
            for col in range(len(s2), - 1, -1):
                if row < len(s1) and s1[row] == s3[row + col] and dp[row + 1][col]:
                    dp[row][col] = True
                if col < len(s2) and s2[col] == s3[row + col] and dp[row][col + 1]:
                    dp[row][col] = True
        return dp[0][0]