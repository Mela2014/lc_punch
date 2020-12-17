class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        rslt = []
        def backtracking(temp, cand):
            if not cand:
                rslt.append(temp)
            for i, num in enumerate(cand):
                backtracking(temp+[num], cand[:i]+cand[i+1:])
        backtracking([], nums)
        return rslt
