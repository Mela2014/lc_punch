class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        maps = {0:-1}
        target = sum(nums)%p
        curr, rslt = 0, len(nums)
        for i, num in enumerate(nums):
            curr = (curr+num)%p
            maps[curr] = i
            if (curr-target)%p in maps:
                rslt = min(rslt, i-maps[(curr-target)%p])
        return rslt if rslt < len(nums) else -1
