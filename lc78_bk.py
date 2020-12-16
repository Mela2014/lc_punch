class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rslt = [[]]
        def backtracking(i):
            if i == len(nums): return
            for j in range(len(rslt)):
                rslt.append(rslt[j] +[nums[i]])
            backtracking(i+1)
        backtracking(0)
        return rslt
