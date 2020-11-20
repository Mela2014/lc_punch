class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        l_s1, l_s2, rslt = len(s1), len(s2), 0
        dp = [[0]*(l_s2 + 1) for _ in range(l_s1 + 1)]
        for i in range(1, l_s1+1): dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        for j in range(1, l_s2+1): dp[0][j] = dp[0][j-1] + ord(s2[j-1])
        for i, c1 in enumerate(s1):
            for j, c2 in enumerate(s2):
                if c1 == c2:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i+1][j] +ord(c2), dp[i][j+1] + ord(c1))
        return dp[-1][-1]