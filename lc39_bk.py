class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        rslt, n = [], len(candidates)
        candidates.sort()
        def backtracking(target, i,curr):
            if target == 0:
                rslt.append(curr)
            elif i < n and target >= candidates[i]:
                temp = candidates[i]
                backtracking(target-temp, i, curr+[temp])
                backtracking(target, i+1, curr)
        backtracking(target, 0, [])
        return rslt
