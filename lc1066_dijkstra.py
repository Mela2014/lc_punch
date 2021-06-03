class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def md(p1, p2):
            return abs(p1[0] - p2[0])+abs(p1[1] - p2[1])
        heap = [(0, 0, "0"*len(bikes))] # total distance, worker id, bike status
        visited = collections.defaultdict(lambda:float("inf"))
        while heap:
            total, idx, bike_status = heapq.heappop(heap)
            if idx == len(workers):
                return total
            for i, b in enumerate(bikes):
                if bike_status[i] != '1':
                    n_total = total + md(workers[idx], b)
                    n_bike_status = bike_status[:i]+'1'+bike_status[i+1:]
                    if n_total < visited[(idx+1, n_bike_status)]:
                        visited[(idx+1, n_bike_status)] = n_total
                        heapq.heappush(heap,[n_total, idx+1, n_bike_status])
        return -1
