class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for s, t, w in times:
            graph[s].append((w, t))
        hp, dist = [(0, K)], {}
        while hp:
            w, t = heapq.heappop(hp)
            if t in dist: continue
            dist[t] = w
            for wnext, tnext in graph[t]:
                if tnext not in dist:
                    heapq.heappush(hp, (wnext + w, tnext))
        return max(dist.values()) if len(dist) == N else -1
