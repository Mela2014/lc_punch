class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def partition(left, right):
            pivot, l = (left+right)//2, left
            dist_pivot = dist[(points[pivot][0], points[pivot][1])]
            points[right], points[pivot] = points[pivot], points[right]
            for i in range(left, right+1):
                if dist[(points[i][0], points[i][1])] < dist_pivot:
                    points[i], points[l] = points[l], points[i]
                    l += 1
            points[l], points[right] = points[right], points[l]
            return l
        def select(left, right):
            if left == right: return
            pivot = partition(left, right)
            if pivot  == K-1:
                return
            if pivot > K-1:
                select(left, pivot-1)
            else:
                select(pivot+1, right)
            return
        dist = {}
        for x, y in points:
            dist[(x, y)] = x**2 + y**2
        select(0, len(points)-1)
        return points[:K]
