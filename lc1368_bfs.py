class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        heap, visited = [(0, 0, 0)], set()
        nrow, ncol = len(grid), len(grid[0])
        directions = {1:(0, 1), 2:(0, -1), 3:(1, 0), 4:(-1, 0)}
        while heap:
            step, x, y = heapq.heappop(heap)
            if x == nrow-1 and y == ncol-1:
                return step
            if (x, y) in visited: continue
            visited.add((x, y))
            for i in directions:
                nx, ny = x+directions[i][0],  y+directions[i][1]
                if 0 <= nx < nrow and 0 <= ny < ncol:
                    if grid[x][y] == i:
                        heapq.heappush(heap, (step, nx, ny))
                    else:
                        heapq.heappush(heap, (step+1, nx, ny))
        return 0
