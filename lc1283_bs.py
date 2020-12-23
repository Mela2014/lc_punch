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
