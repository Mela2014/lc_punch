class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay): return -1
        left, right = 1, max(bloomDay)
        while left <= right:
            mid = (left + right)//2
            tempf, tempb= 0, 0
            for bD in bloomDay:
                if bD <= mid:
                    tempf += 1
                else:
                    tempf = 0
                if tempf == k:
                    tempb += 1
                    tempf = 0
            if tempb >= m:
                right = mid -1
            else:
                left = mid + 1
        return left
