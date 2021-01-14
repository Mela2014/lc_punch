class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for start, end, w in flights:
            graph[start].append((end, w))
        heap, visitedD, visitedS = [(0, 0, src)], [float("inf")]*n, [float("inf")]*n
        visitedD[src], visitedS[src] = 0, 0
        while heap:
            cost, step, pre = heapq.heappop(heap)
            if pre == dst: return cost
            if step ==  K+1: continue
            for curr, w in graph[pre]:
                if visitedD[curr] > cost + w:
                    visitedD[curr] = cost + w
                    visitedS[curr] = step+1
                    heapq.heappush(heap, (cost+w, step+1, curr))
                elif step < visitedS[curr]:
                    heapq.heappush(heap, (cost+w, step+1, curr))
        return -1
