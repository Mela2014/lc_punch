class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def check(t):
            rslt, temp = 0, 0
            for w in weights:
                temp += w
                if temp > t:
                    rslt += 1
                    temp = w
            return rslt+1

        left, right = max(weights), sum(weights)
        while left <= right:
            mid = (left + right)//2
            if check(mid) > D:
                left = mid + 1
            else:
                right = mid -1
        return left
