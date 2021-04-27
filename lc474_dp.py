class Solution:
    def findMaxForm(self, strs, m, n):
        xy = [[s.count("0"), s.count("1")] for s in strs]

        @lru_cache(None)

        def dp(mm, nn, kk):
            if mm < 0 or nn < 0: return -float("inf")
            if kk == len(strs): return 0
            x, y = xy[kk]
            return max(1 + dp(mm-x, nn-y, kk + 1), dp(mm, nn, kk + 1))

        return dp(m, n, 0)

    def findMaxForm(self, strs, m, n):
        dp = [[0]*(m+1) for _ in range(n+1)]
        for s in strs:
            ones, zeros = s.count("1"), s.count("0")
            for i in range(n, ones-1, -1):
                for j in range(m, zeros-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-ones][j-zeros]+1)
        return dp[n][m]
