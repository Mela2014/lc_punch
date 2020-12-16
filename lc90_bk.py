class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rslt = []
        def backtracking(temp, i):
            rslt.append(temp)
            for j, num in enumerate(nums[i:]):
                if j == 0 or num != nums[j+i-1]:
                    backtracking(temp+[num], i+j+1)
        backtracking([], 0)
        return rslt
                
