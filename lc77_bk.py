class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        rslt = []
        def backtracking(temp, i):
            if len(temp) == k:
                rslt.append(temp)
                return
            if i == n: return
            for t in range(i, n):
                backtracking(temp+[t+1], t+1)
        backtracking([], 0)
        return rslt
