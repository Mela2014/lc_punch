class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l_s1, l_s2 = len(s1), len(s2)
        if len(s3) != l_s1 + l_s2:
            return False
        dp = [[False]*(l_s2 + 1) for _ in range(l_s1 + 1)]
        for i in range(l_s1 + 1):
            for j in range(l_s2 + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                    continue
                if i > 0 and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i-1][j]
                if j > 0 and  s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i][j-1]
                
        return dp[-1][-1]