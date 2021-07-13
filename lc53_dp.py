class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp, rslt = nums[0], nums[0]
        for num in nums[1:]:
            temp = max(temp + num, num)
            rslt = max(temp, rslt)
        return rslt
