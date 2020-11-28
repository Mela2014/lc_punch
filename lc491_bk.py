class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        rslt = []
        def backtracking(stk, candidate):
            if len(stk) >= 2:
                rslt.append(stk)
            if not candidate:
                return
            seen = set()
            for i, cand in enumerate(candidate):
                if cand in seen:
                    continue
                if not stk or stk[-1] <= candidate[i]:
                    seen.add(cand)
                    backtracking(stk+[cand], candidate[i+1:])
        backtracking([], nums)
        return rslt
