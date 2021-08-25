class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        rslt, n = 0, len(nums)
        for i, num in enumerate(nums):
            rslt ^= num
            rslt ^= i
        rslt ^= n
        return rslt
