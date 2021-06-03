class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left = 0
        right = maxSum
        while left < right:
            mid = right - (right - left) // 2
            extra1 = mid - 1 - index
            extra1 = (extra1 + 1) * extra1 // 2 if extra1 > 0 else extra1
            extra2 = mid - 1 - (n - index - 1)
            extra2 = (extra2 + 1) * extra2 // 2 if extra2 > 0 else extra2
            lower = (mid - 1) * mid // 2 - extra1
            upper = (mid - 1) * mid // 2 - extra2
            if lower + mid + upper > maxSum:
                right = mid - 1
            else:
                left = mid
        return left


    def maxValue(self, n, index, maxSum):
        def test(a):
            b = max(a - index, 0)
            res = (a + b) * (a - b + 1) / 2
            b = max(a - ((n - 1) - index), 0)
            res += (a + b) * (a - b + 1) / 2
            return res - a

        maxSum -= n
        left, right = 0, maxSum
        while left < right:
            mid = (left + right + 1) / 2
            if test(mid) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left + 1
