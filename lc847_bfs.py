class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        visited, n = set(), len(graph)
        final = (1 << n)-1
        dque = collections.deque([(1 << i, i) for i in range(n)])
        step = 0
        while dque:
            size = len(dque)
            for _ in range(size):
                state, x  = dque.popleft()
                if state == final:
                    return step
                for y in graph[x]:
                    if (state|(1<< y), y) not in visited:
                        dque.append((state|(1<< y), y))
                        visited.add((state|(1<< y), y))
            step += 1
        return -1
