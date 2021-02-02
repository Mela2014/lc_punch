class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        directions = {"d":(1, 0), "l":(0, -1), "r":(0, 1),"u":(-1, 0)}
        heap, visited = [(0,"", ball[0], ball[1])], set()
        nrow, ncol = len(maze), len(maze[0])
        while heap:
            step, path, currx, curry = heapq.heappop(heap)
            if currx == hole[0] and curry == hole[1]:
                return path
            if (currx, curry) in visited:
                continue
            visited.add((currx, curry))
            for dr in ["d", "l", "r", "u"]:
                dx, dy = directions[dr]
                tx, ty, l = currx, curry, 0
                while 0 <= tx+dx < nrow and 0 <= ty+dy < ncol and maze[tx+dx][ty+dy] == 0:
                    tx += dx
                    ty += dy
                    l  += 1
                    if tx == hole[0] and ty == hole[1]:
                        break
                heapq.heappush(heap, (step+l, path+dr, tx, ty))
        return "impossible"
