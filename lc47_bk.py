class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        rslt = []
        nums.sort()
        def backtracking(temp, cand):
            if not cand:
                rslt.append(temp)
            for i, num in enumerate(cand):
                if i != 0 and num == cand[i-1]:
                    continue
                backtracking(temp+[num], cand[:i]+cand[i+1:])
        backtracking([], nums)
        return rslt
