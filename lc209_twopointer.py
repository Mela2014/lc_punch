class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        curr, rslt, left = 0, len(nums)+1, 0
        for right, num in enumerate(nums):
            curr += num
            if curr >= s:
                while curr >= s:
                    rslt = min(right-left+1, rslt)
                    curr -= nums[left]
                    left += 1
        return 0 if rslt == len(nums)+1 else rslt
