class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        maps = {0:-1}
        presum = 0
        for i, num in enumerate(nums):
            presum += num
            presum = presum%k
            if presum in maps and i-maps[presum] > 1:
                return True
            elif presum not in maps:
                maps[presum] = i
        return False
        
