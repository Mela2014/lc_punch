class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        heap, visited = [(0, start[0], start[1])], {}
        rslt = float("inf")
        nrow, ncol = len(maze), len(maze[0])
        while heap:
            step, currx, curry = heapq.heappop(heap)
            visited.add((currx, curry))
            if currx == destination[0] and curry == destination[1]:
                return step
            for dx, dy in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                tx, ty, l = currx, curry, 0
                while 0 <= tx+dx < nrow and 0 <= ty+dy < ncol and maze[tx+dx][ty+dy] == 0:
                    tx += dx
                    ty += dy
                    l  += 1
                if (tx, ty) not in visited:
                    heapq.heappush(heap, (step+l, tx, ty))
        return -1


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        heap, visited = [(0, start[0], start[1])], {(start[0], start[1]): 0}
        nrow, ncol = len(maze), len(maze[0])
        while heap:
            step, currx, curry = heapq.heappop(heap)
            if currx == destination[0] and curry == destination[1]:
                return step
            for dx, dy in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                tx, ty, l = currx, curry, 0
                while 0 <= tx+dx < nrow and 0 <= ty+dy < ncol and maze[tx+dx][ty+dy] == 0:
                    tx += dx
                    ty += dy
                    l  += 1
                if (tx, ty) not in visited or visited[(tx, ty)] > step+l:
                    visited[(tx, ty)] = step + l
                    heapq.heappush(heap, (step+l, tx, ty))
        return -1
