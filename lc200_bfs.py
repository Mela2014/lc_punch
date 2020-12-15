class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        n_row, n_col = len(grid), len(grid[0])
        queue, rslt = collections.deque(), 0
        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == "1":
                    grid[i][j] = None
                    queue.append((i, j))
                    while queue:
                        curr_i, curr_j = queue.popleft()
                        for x, y  in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                                t_x, t_y = curr_i+x, curr_j + y
                                if t_x >= 0 and t_x < n_row and t_y >= 0 and t_y < n_col and grid[t_x][t_y] == "1":
                                    grid[t_x][t_y] = None
                                    queue.append((t_x, t_y))

                    rslt += 1
        return rslt 
