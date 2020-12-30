class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        @lru_cache(None)
        def dfs(d, t):
            if d*f < t or d > t:
                return 0
            if d== 0 and t == 0:
                return 1
            rslt = 0
            for j in range(1, f+1):
                rslt += dfs(d-1, t-j)
            return rslt
        return dfs(d, target)%(10**9+7)
