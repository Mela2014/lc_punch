class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        def check(mid):
            cuts, curr = 0, 0
            for s in sweetness:
                curr += s
                if curr >= mid:
                    cuts += 1
                    curr = 0
            return cuts

        if len(sweetness) == K+1: return min(sweetness)
        left, right = min(sweetness), sum(sweetness)
        rslt = left
        while left <= right:
            mid = (left + right)//2
            if check(mid) > K:
                left = mid + 1
            else:
                right = mid - 1
        return right
        
