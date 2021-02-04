class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if not nums: return False
        if len(nums) == 1: return 23.9 < nums[0] < 24.1
        for i in range(len(nums)):
            for j in range(i):
                if i > j:
                    nums_next = nums[:j]+nums[j+1:i]+nums[i+1:]
                    for op in (truediv, mul, add, sub):
                        if op is not truediv or nums[j]:
                            nums_next.append(op(nums[i], nums[j]))
                            if self.judgePoint24(nums_next): return True
                            nums_next.pop()
                        if op in (add, mul): continue
                        if op is sub or nums[i]:
                            nums_next.append(op(nums[j], nums[i]))
                            if self.judgePoint24(nums_next): return True
                            nums_next.pop()
        return False
