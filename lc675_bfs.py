class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        nrow, ncol, rslt = len(forest), len(forest[0]), 0
        heap = []
        for i in range(nrow):
            for j in range(ncol):
                if forest[i][j] > 0:
                    heapq.heappush(heap, (forest[i][j], i, j))
        def bfs(nextval, nextx, nexty, currx, curry):
            dque, seen, step = collections.deque([(currx, curry)]), {(currx, curry)}, 0
            while dque:
                size = len(dque)
                for _ in range(size):
                    x,y = dque.popleft()
                    if x == nextx and y == nexty:
                        return step
                    for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                        if 0 <= nx < nrow and 0 <= ny < ncol and forest[nx][ny] > 0 and (nx, ny) not in seen:
                            seen.add((nx, ny))
                            dque.append((nx, ny))
                step += 1
            return -1

        currx, curry, visited = 0, 0, {(0, 0)}
        while heap:
            nextval, nextx, nexty = heapq.heappop(heap)
            step = bfs(nextval, nextx, nexty, currx, curry)
            if step  == -1: return -1
            rslt += step
            currx, curry = nextx, nexty
        return rslt
