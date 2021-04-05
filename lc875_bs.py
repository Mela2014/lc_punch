class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(n):
            return sum((x-1)//n+1 for x in piles)
        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right)//2
            if check(mid) <= h:
                right = mid - 1
            else:
                left =  mid + 1
        return left
