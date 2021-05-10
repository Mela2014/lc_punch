class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        @lru_cache(None)
        def dfs(i):
            rslt = 1
            for direction in [-1, 1]:
                for j in range(i+direction, i+d*direction+direction, direction):
                    if j < 0 or j >= n or arr[j] >= arr[i]: break
                    rslt = max(rslt, dfs(j)+1)
            return rslt
        return max(map(dfs, range(n)))
        
