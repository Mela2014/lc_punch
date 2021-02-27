class Solution:
    def integerBreak(self, n: int) -> int:
        @functools.lru_cache(None)
        def dfs(j):
            if j <= 2:
                return 1
            else:
                rslt = 0
                for i in range(1, j):
                    rslt = max(rslt, i*max(dfs(j-i),j-i))
                return rslt
        return dfs(n)
    def integerBreak(self, n:int) -> int:
        dp = [1]*(n+1)
        for j in range(3, n+1):
            for i in range(1, j):
                dp[j] = max(dp[j], i*max(dp[j-i], j-i))
        return dp[n]
