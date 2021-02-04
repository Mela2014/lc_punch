class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        toCover, nrow, ncol = 0, len(grid), len(grid[0])
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 0: toCover += 1
                if grid[i][j] == 1: start = (i,j)
        self.rslt = 0
        def backtracking(i, j, step):
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if x < 0 or x >= nrow or y < 0 or y >= ncol or grid[x][y] < 0: continue
                if grid[x][y] == 0:
                    grid[x][y] = -2
                    backtracking(x, y, step + 1)
                    grid[x][y] = 0
                elif grid[x][y] == 2 and step == toCover:
                    self.rslt += 1
        backtracking(start[0], start[1], 0)
        return self.rslt
