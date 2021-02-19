class Solution:
    def countArrangement(self, n: int) -> int:
        ini = (1 << n)-1
        @lru_cache(None)
        def dfs(i, bitmask):
            if i == n+1:
                return 1
            elif bitmask == 0:
                return 0
            rslt = 0
            for j in range(n):
                if (1 << j) & bitmask and ((j+1)%i == 0 or i%(j+1) == 0):
                    rslt += dfs(i+1, bitmask & (~(1 << j)))
            return rslt
        return dfs(1, ini)
