class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def eatingHour(k):
            return sum( (x-1)//k + 1 for x in piles)
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right)//2
            if eatingHour(mid) > H:
                left = mid
            else:
                right = mid
            if (left + right)//2 == mid:
                left += 1
        return right
