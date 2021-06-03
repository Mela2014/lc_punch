class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        directions = {'U':'D', 'D':'U', 'L':'R', 'R':'L'}
        steps = {'U':(-1, 0), 'D':(1, 0), 'L':(0, -1), 'R':(0, 1)}
        self.target = None
        graph = {(0, 0): 0}
        # backtracking build graph
        def backtracking(x, y):
            if master.isTarget(): self.target = (x, y)
            for d in directions:
                nx, ny = x + steps[d][0], y+steps[d][1]
                if (nx, ny) in graph: continue
                if master.canMove(d):
                    graph[(nx, ny)] = master.move(d)
                    backtracking(nx, ny)
                    master.move(directions[d])
        backtracking(0, 0)
        if self.target is None: return -1
        # bfs find rslt
        heap = [[0, 0, 0]] # cost, x, y
        seen = collections.defaultdict(lambda: float("inf"))
        while heap:
            cost, x, y = heapq.heappop(heap)
            if (x, y) == self.target: return cost
            for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if (nx, ny) in graph and cost + graph[(nx, ny)] < seen[(nx, ny)] :
                        seen[(nx, ny)] = cost + graph[(nx, ny)]
                        heapq.heappush(heap, (cost + graph[(nx, ny)], nx, ny))
        return -1
