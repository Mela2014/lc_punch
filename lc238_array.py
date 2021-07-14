class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rslt = [1]*n
        for i in range(1, n):
            rslt[i] = rslt[i-1]*nums[i-1]
        curr = 1
        for i in range(n-2, -1, -1):
            curr *= nums[i+1]
            rslt[i] = rslt[i]*curr
        return rslt
