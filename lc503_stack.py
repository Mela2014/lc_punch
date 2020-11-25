class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums: return nums
        rslt, stk = [-1]*len(nums), []
        for i in range(len(nums)-1, -len(nums), -1):
            while stk and stk[-1] <= nums[i]:
                stk.pop()
            if stk: rslt[i] = stk[-1]
            stk.append(nums[i])
        return rslt
