class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        rslt, n = [], len(S)
        def backtracking(i, curr):
            if i == n:
                rslt.append(curr)
            else:
                x = S[i]
                for y in {x.upper(), x.lower()}:
                    backtracking(i+1, curr+y)
        backtracking(0, "")
        return rslt
