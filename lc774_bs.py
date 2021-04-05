class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        def check(p):
            count = 0
            for i in range(1, n):
                count += int((stations[i]-stations[i-1])/p)
            return count

        left, right, n =0, 0, len(stations)
        for i in range(1, n):
            right = max(right, stations[i]-stations[i-1])
        while left < right - 1e-6:
            mid = (left + right)/2
            if check(mid) > k:
                left = mid
            else:
                right = mid
        return left
