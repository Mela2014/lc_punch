class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        last, n = 0, len(nums)
        for i in range(n):
            if nums[i] >= n-i > last:
                return n-i
            last = nums[i]
        return -1
        
