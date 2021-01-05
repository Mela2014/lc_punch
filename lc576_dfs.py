class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        memo = {}
        def dfs(x, y, step):
            if (x, y, step) in memo: return memo[(x, y, step)]
            if (x < 0 or x >= m or y < 0 or y >= n): return 1
            if step == 0:  return 0
            rslt = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                rslt += dfs(x+dx, y+dy, step-1)
            memo[(x, y, step)] = rslt
            return rslt
        return dfs(i, j, N)%(10**9+7)
