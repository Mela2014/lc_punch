class Solution:
    def jump(self, nums: List[int]) -> int:
        rslt, last, curr = 0, 0, 0
        for i, num in enumerate(nums[:-1]):
            curr = max(curr, i+num)
            if i == last:
                rslt += 1
                last = curr
            if last >= len(nums)-1:
                break
        return rslt

        
