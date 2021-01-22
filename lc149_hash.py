# Euclidean Algorithm : GCD
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a
        n, rslt = len(points), 0
        for i in range(n):
            slopemap, dup, tmax = collections.defaultdict(int), 0, 0
            if rslt > n-i: break
            for j in range(i+1, n):
                dx, dy = points[j][0]-points[i][0], points[j][1] - points[i][1]
                if dx == 0 and dy == 0:
                    dup += 1
                    continue
                currgcd = gcd(dx, dy)
                slope = (dx//currgcd, dy//currgcd)
                slopemap[slope] += 1
                tmax = max(slopemap[slope], tmax)
            rslt = max(rslt, tmax+dup+1)
        return rslt
