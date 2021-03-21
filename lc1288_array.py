class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[0], -x[1]))
        last, cnt = -1, 0
        for x, y in intervals:
            if y > last:
                last = y
                cnt += 1
        return cnt
                
