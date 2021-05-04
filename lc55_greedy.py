class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return True
        nxt = 0
        for i, num in enumerate(nums):
            if i+num > nxt:
                nxt = i+num
            if nxt == i:
                break
        return nxt >= len(nums)-1

        
