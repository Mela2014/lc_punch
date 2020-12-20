class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total, left, rslt = sum(nums), 0, len(nums)+1
        if total < x:
            return -1
        for right, num in enumerate(nums):
            total -= num
            while total < x:
                total += nums[left]
                left += 1
            if total == x:
                rslt = min(rslt, len(nums)-right-1+left)
        return rslt if rslt < len(nums)+1 else -1
