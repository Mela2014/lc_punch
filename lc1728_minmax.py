class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        nrow, ncol, thred = len(grid), len(grid[0]), 0
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == "C": catloc = (i, j)
                if grid[i][j] == "M": mouseloc = (i, j)
                if grid[i][j] == "F": foodloc = (i, j)
                if grid[i][j] != "#": thred += 1
        @lru_cache(None)
        def dfs(cat, mouse, step):
            if cat == mouse or cat == foodloc or step > 2*thred:
                return False
            if mouse == foodloc:
                return True
            if step%2 == 0:
                for nmouse in nextstep(mouse, mouseJump):
                    if dfs(cat, nmouse, step + 1):
                        return True
                return False
            else:
                for ncat in nextstep(cat, catJump):
                    if not dfs(ncat, mouse, step+1):
                        return False
                return True

        def nextstep(curr, step):
            rslt = []
            for dx, dy in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                for jump in range(step+1):
                    nx, ny = curr[0]+dx*jump, curr[1]+dy*jump
                    if 0 <= nx < nrow and 0 <= ny < ncol and grid[nx][ny] != "#":
                        rslt.append((nx, ny))
                    else:
                        break
            return rslt

        return dfs(catloc, mouseloc, 0)
