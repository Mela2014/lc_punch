class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        rslt, last = 0, -float("inf")
        for point in points:
            if point[0] <= last:
                last = min(last, point[1])
            else:
                rslt += 1
                last = point[1]
        return rslt

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(reverse = True)
        rslt, last = 0, float("inf")
        for point in points:
            if point[1] >= last:
                last = max(last, point[0])
            else:
                rslt += 1
                last = point[0]
        return rslt
