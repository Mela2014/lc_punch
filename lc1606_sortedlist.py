from sortedcontainers import SortedList
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        freq = [0]*k
        n = len(arrival)
        busy = []
        free = SortedList(range(k))
        for i in range(n):
            while busy and busy[0][0] <= arrival[i]:
                t, si = heapq.heappop(busy)
                free.add(si)
            if free:
                idx = free.bisect_left(i%k)%len(free)
                s = free.pop(idx)
                freq[s] += 1
                heapq.heappush(busy, (arrival[i]+load[i], s))
        mx = max(freq)
        return [x for x in range(k) if freq[x] == mx]
