class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        left, right = target//len(arr), max(arr)
        def check(mid):
            rslt = 0
            for num in arr:
                if num < mid:
                    rslt += num
                else:
                    rslt += mid
            return rslt
        while left <= right:
            mid = (left + right)//2
            if check(mid) <= target:
                left = mid + 1
            else:
                right = mid - 1
        return left if abs(check(left)-target) < abs(check(right)-target) else right
