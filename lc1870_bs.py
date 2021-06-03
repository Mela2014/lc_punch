class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour < len(dist) - 1: return -1
        left, right = 1, int(100000/0.01)
        def check(mid):
            rslt = 0
            for d in dist[:-1]:
                rslt += (d-1)//mid + 1
            return rslt + dist[-1]/mid
        while left <= right:
            mid = (left + right)//2
            temp = check(mid)
            if temp <= hour:
                right  = mid - 1
            else:
                left = mid + 1
        return int(left) if check(left) <= hour else -1
