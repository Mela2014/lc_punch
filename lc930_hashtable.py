class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        prefix, rslt, temp = 0, 0, {0:1}
        for i, x in enumerate(A):
            prefix += x
            if prefix-S in temp:
                rslt += temp[prefix-S]
            temp[prefix] = temp.get(prefix, 0)+1
        return rslt
    
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        left_lo, left_hi = 0, 0
        last_lo, last_hi = 0, 0
        rslt = 0
        for right, num in enumerate(nums):
            last_lo += num
            last_hi += num

            while left_lo < right and last_lo > goal:
                last_lo -= nums[left_lo]
                left_lo += 1
            while left_hi < right and (last_hi > goal or (last_hi == goal and nums[left_hi] == 0)):
                last_hi -= nums[left_hi]
                left_hi += 1

            if last_lo == goal:
                rslt += left_hi - left_lo + 1
        return rslt
