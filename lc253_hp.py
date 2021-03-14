class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        hq = []
        for itv in intervals:
            if hq and itv[0] >= hq[0]:
                heapq.heappop(hq)
            heapq.heappush(hq, itv[1])
        return len(hq)
