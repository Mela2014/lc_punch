class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        maps = {(0, 0)}
        ops = {"U":"D", "D":"U", "L":"R", "R":"L"}
        steps = {"U":(1, 0), "D":(-1, 0), "L":(0, -1), "R":(0, 1)}
        self.target = None
        def buildmap(x, y):
            if master.isTarget(): self.target = (x, y)
            for d in steps:
                nx, ny = x + steps[d][0], y+steps[d][1]
                if (nx, ny) in maps: continue
                if master.canMove(d):
                    master.move(d)
                    maps.add((nx, ny))
                    buildmap(nx, ny)
                    master.move(ops[d])
        buildmap(0, 0)
        if self.target is None: return -1
        queue = collections.deque([(0, 0)])
        rslt = 0
        seen = {(0, 0)}
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if (x, y) == self.target: return rslt
                for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                    if (nx, ny) in maps and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        queue.append((nx, ny))
            rslt += 1
        return -1
