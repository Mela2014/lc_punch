class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            curr = 1
            for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if 0 <= i+x < len(grid) and 0<=j + y < len(grid[0]) and grid[i+x][j+y] == 1:
                    grid[i+x][j+y] = 0
                    curr += dfs(i+x, j+y)
            return curr
        rslt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    rslt = max(rslt, dfs(i, j))
        return rslt
