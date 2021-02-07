class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        n, rslt = len(digits), []
        cmap = {"2":"abc", "3":"def", "4":"ghi",
                "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        def btrack(i, curr):
            if i == n:
                rslt.append(curr)
            else:
                for c in cmap[digits[i]]:
                    btrack(i+1, curr+c)
        btrack(0, "")
        return rslt 
