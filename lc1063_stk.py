class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        stk = []
        rslt = 0
        for i in range(n):
            while stk and nums[i] < nums[stk[-1]]:
                rslt += i- stk.pop()
            stk.append(i)
        while stk:
            rslt += n-stk.pop()
        return rslt
