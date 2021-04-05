class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, sum(nums)
        while left <= right:
            mid = (left + right)//2
            rslt =  sum(ceil(x/mid) for x in nums)
            if rslt > threshold:
                left = mid
            else:
                right = mid - 1
            if mid == (left+right)//2:
                left += 1
        return left

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(i):
            rslt = 0
            for n in nums:
                rslt += (n-1)//i + 1
            return rslt
        left, right = 1, max(nums)
        while left <= right:
            mid = (left + right)//2
            if check(mid) <= threshold:
                right = mid -1
            else:
                left = mid + 1
        return left
