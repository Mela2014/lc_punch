class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        dp = [[0]*(l1 +1) for _ in range(l2+1)]
        for j in range(l2+1): dp[j][0] = j
        for i in range(l1+1): dp[0][i] = i
        for i, c1 in enumerate(word1):
            for j, c2 in enumerate(word2):
                if c1 == c2:
                    dp[j+1][i+1] = dp[j][i]
                else:
                    dp[j+1][i+1] = min(dp[j][i+1], dp[j+1][i], dp[j][i]) +1
        return dp[-1][-1]