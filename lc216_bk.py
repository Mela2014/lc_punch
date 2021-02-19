class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n < k*1 or n > k*9: return []
        rslt = []
        def backtracking(i, n, curr):
            if n == 0 and len(curr) == k:
                rslt.append(curr)
            elif len(curr) < k and i < 10:
                for j in range(i, 10):
                    backtracking(j+1, n-j, curr + [j])
        backtracking(1, n, [])
        return rslt

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n < k*1 or n > k*9: return []
        rslt = []
        def backtracking(i, n, curr):
            if n == 0 and len(curr) == k:
                rslt.append(curr)
            elif len(curr) < k and i < 10:
                backtracking(i+1, n, curr)
                backtracking(i+1, n-i, curr + [i])
        backtracking(1, n, [])
        return rslt
    
