class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return []
        rslt, n = [], len(candidates)
        candidates.sort()
        def backtracking(i, target, curr):
            if target == 0:
                rslt.append(curr)
            elif i < n and target > 0:
                temp = candidates[i]
                backtracking(i+1, target-temp, curr+[temp])
                while i < n-1 and candidates[i] == candidates[i+1]:
                    i += 1
                backtracking(i+1, target, curr)
        backtracking(0, target, [])
        return rslt
