class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        rslt = [intervals[0]]
        for x, y in intervals[1:]:
            if x > rslt[-1][1]:
                rslt.append([x, y])
            else:
                rslt[-1][0], rslt[-1][1] = min(rslt[-1][0], x), max(rslt[-1][1], y)
        return rslt

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals are initially sorted
        rslt, mark = [], True
        for i, (x, y) in enumerate(intervals):
            if y < newInterval[0]:
                rslt.append([x, y])
            elif x > newInterval[1]:
                rslt.append(newInterval)
                return rslt + intervals[i:]
            else:
                newInterval[0], newInterval[1] = min(x, newInterval[0]), max(y, newInterval[1])
        return rslt
