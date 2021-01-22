class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        dque, visited = collections.deque([tuple(start)]), {tuple(start)}
        n, c = len(maze), len(maze[0])
        while dque:
            currow, curcol = dque.popleft()
            if destination[0] == currow and destination[1] == curcol: return True
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                tx, ty = currow, curcol
                while 0 <= tx+x < n and 0 <= ty+y < c and maze[tx+x][ty+y] == 0:
                        tx += x
                        ty += y
                if (tx, ty) not in visited:
                    dque.append((tx, ty))
                    visited.add((tx, ty))
        return False
