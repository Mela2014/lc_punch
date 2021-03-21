class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        rslt = []
        for x, y in intervals:
            if x < toBeRemoved[0] and y <= toBeRemoved[1]:
                rslt.append([x, min(toBeRemoved[0], y)])
            elif x >= toBeRemoved[0] and y > toBeRemoved[1]:
                rslt.append([max(x, toBeRemoved[1]), y])
            elif x < toBeRemoved[0] and y > toBeRemoved[1]:
                rslt.append([x, toBeRemoved[0]])
                rslt.append([toBeRemoved[1], y])
        return rslt
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        rslt = []
        for x, y in intervals:
            if y < toBeRemoved[0] or x > toBeRemoved[1]:
                rslt.append([x, y])
            else:
                if x < toBeRemoved[0]:
                    rslt.append([x, toBeRemoved[0]])
                if y > toBeRemoved[1]:
                    rslt.append([toBeRemoved[1], y])
        return rslt
