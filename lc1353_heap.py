class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        rslt, last = 0, 0
        heap = []
        i = 0
        while i < len(events) or heap:
            if not heap: last = events[i][0]
            if i < len(events) and events[i][0] <= last <= events[i][1]:
                heapq.heappush(heap, events[i][1])
                i += 1
            elif i < len(events) and events[i][1] < last:
                i += 1
                continue
            elif heap:
                temp = heapq.heappop(heap)
                if temp >= last:
                    rslt += 1
                    last += 1
        return rslt
