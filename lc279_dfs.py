class Solution:
    def numSquares(self, n: int) -> int:
        cands = [i**2 for i in range(1, int(n**0.5)+1)]
        @lru_cache(None)
        def dfs(i):
            if i in cands:
                return 1
            rslt = float("inf")
            for cand in cands:
                if cand > i:
                    break
                rslt = min(rslt, dfs(i-cand)+1)
            return rslt
        return dfs(n)

class Solution:
    def numSquares(self, n: int) -> int:
        cands = [i*i for i in range(int(n**0.5) + 1)]
        dp = [float("inf")]*(n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for cand in cands:
                if i < cand:
                    break
                dp[i] = min(dp[i], dp[i-cand] + 1)
        return dp[-1]
