class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        holder = {0:-1}
        curr = 0
        rslt = 0
        for i, num in enumerate(nums):
            curr += num
            if curr - k in holder:
                rslt = max(rslt, i - holder[curr-k])
            if curr not in holder:
                holder[curr] = i
        return rslt
