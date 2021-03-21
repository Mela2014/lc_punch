class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 0: return 0
        intervals.sort()
        last, rslt = intervals[0][1], 0
        for x, y in intervals[1:]:
            if x < last:
                rslt += 1
                if y < last:
                    last = y
            else:
                last = y
        return rslt
