class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n, rslt = len(grid), 0
        maps = [[[0,0,0,0] for _ in range(n)] for _ in range(n)]
        def dfs(i, j, k):
            if 0 <= i < n and 0 <= j < n and not maps[i][j][k]:
                if grid[i][j] == "\\":
                    if k < 2:
                        maps[i][j][0] = maps[i][j][1] = rslt
                        dfs(i-1, j, 2)
                        dfs(i, j+1, 3)
                    else:
                        maps[i][j][2] = maps[i][j][3] = rslt
                        dfs(i, j-1, 1)
                        dfs(i+1, j, 0)
                elif grid[i][j] == "/":
                    if k == 0 or k == 3:
                        maps[i][j][0] = maps[i][j][3] = rslt
                        dfs(i-1, j, 2)
                        dfs(i, j-1, 1)
                    else:
                        maps[i][j][1] = maps[i][j][2] = rslt
                        dfs(i, j+1, 3)
                        dfs(i+1, j, 0)
                else:
                    maps[i][j] = [rslt]*4
                    dfs(i, j-1, 1)
                    dfs(i, j+1, 3)
                    dfs(i-1, j, 2)
                    dfs(i+1, j, 0)
        for i in range(n):
            for j in range(n):
                for k in range(4):
                    if not maps[i][j][k]:
                        rslt += 1
                        dfs(i, j, k)
        return rslt
