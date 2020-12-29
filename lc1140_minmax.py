class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}
        def dfs(i, m):
            if (i, m) in memo:
                return memo[(i, m)]
            if i+2*m >= len(piles):
                return sum(piles[i:])
            rslt = float("inf")
            for j in range(i+1, i+2*m+1):
                rslt = min(rslt, dfs(j, max(j-i, m)))
            memo[(i, m)] = sum(piles[i:]) - rslt
            return memo[(i, m)]
        return dfs(0, 1)

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, m):
            if i+2*m >= len(piles):
                return sum(piles[i:])
            rslt = float("inf")
            for j in range(i+1, i+2*m+1):
                rslt = min(rslt, dfs(j, max(j-i, m)))
            return sum(piles[i:]) - rslt
        return dfs(0, 1)
