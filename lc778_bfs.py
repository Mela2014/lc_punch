class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited, heap, n = {(0,0)}, [(grid[0][0], 0, 0)], len(grid)
        rslt = 0
        while heap:
            node, x, y  = heapq.heappop(heap)
            rslt = max(rslt, node)
            if x == n-1 and y == n-1:
                return rslt
            for i, j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= i < n and 0 <= j < n and (i, j) not in visited:
                    heapq.heappush(heap, (grid[i][j], i, j))
                    visited.add((i, j))
        return rslt
