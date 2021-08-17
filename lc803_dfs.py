class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                rslt = 1
                grid[i][j] = 2
                rslt += sum(dfs(x, y) for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)])
                return rslt
            return 0

        def is_new_stable(i, j):
            return i== 0 or any([0 <= x < m and 0 <= y < n and grid[x][y] == 2 for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]])

        for i, j in hits:
            grid[i][j] -= 1

        for i in range(n):
            dfs(0, i)

        res = [0]*len(hits)
        for k in range(len(hits)-1, -1, -1):
            i, j = hits[k]
            grid[i][j] += 1
            if grid[i][j] == 1 and is_new_stable(i, j):
                res[k] = dfs(i, j)-1
        return res
