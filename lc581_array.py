class Solution(object):
    def findUnsortedSubarray(self, nums):
        n = len(nums)
        if n < 2: return 0
        l, r = 0, n - 1
        while l < n - 1 and nums[l] <= nums[l + 1]:
            l += 1
        while r > 0 and nums[r] >= nums[r -1]:
            r -= 1
        if l > r: return 0
        subarray = nums[l:r+1]
        mi, ma = min(subarray), max(subarray)

        while l > 0 and mi < nums[l-1]:
            l -= 1
        while r < n - 1 and ma > nums[r+1]:
            r += 1
        return r - l + 1
