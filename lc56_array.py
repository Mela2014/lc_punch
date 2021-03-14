class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        rslt = []
        for it in intervals:
            if not rslt:
                rslt.append(it)
            elif it[0] <= rslt[-1][1]:
                rslt[-1][1] = max(rslt[-1][1], it[1])
            else:
                rslt.append(it)
        return rslt
