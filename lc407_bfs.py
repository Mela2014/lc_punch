class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        heap, visited = [], set()
        nrow, ncol = len(heightMap), len(heightMap[0])
        for i in range(nrow):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][ncol-1], i, ncol-1))
            visited |= {(i, 0), (i, ncol-1)}
        for j in range(ncol):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, (heightMap[nrow-1][j], nrow-1, j))
            visited |= {(0, j), (nrow-1, j)}
        rslt = 0
        while heap:
            border, x, y = heapq.heappop(heap)
            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 < nx < nrow-1 and 0 < ny < ncol-1 and (nx, ny) not in visited:
                    rslt += max(0, border-heightMap[nx][ny])
                    visited.add((nx, ny))
                    heapq.heappush(heap, (max(border, heightMap[nx][ny]), nx, ny))
        return rslt
