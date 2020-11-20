class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l_w1, l_w2 = len(word1), len(word2)
        dp = [[0]*(l_w2+1) for _ in range(l_w1+1)]
        for i in range(1, l_w1+1): dp[i][0] = dp[i-1][0]+1
        for j in range(1, l_w2+1): dp[0][j] = dp[0][j-1]+1
        
        for i, c1 in enumerate(word1):
            for j, c2 in enumerate(word2):
                if c1 == c2:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1])+1
        return dp[-1][-1]