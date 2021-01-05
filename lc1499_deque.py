class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        dque, rslt = collections.deque(), -float("inf")
        for idx, point in enumerate(points):
            while dque and point[0] - points[dque[0]][0] > k:
                dque.popleft()
            if dque: rslt = max(rslt, points[dque[0]][1]-points[dque[0]][0]+point[1]+point[0])
            while dque and points[dque[-1]][1]-points[dque[-1]][0] <= point[1]-point[0]:
                dque.pop()
            dque.append(idx)
        return rslt
