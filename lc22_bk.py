class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        rslt, m = [], 2*n
        def backtracking(curr, left, right):
            if left+right == m:
                rslt.append(curr)
            else:
                if left < m -left:
                    backtracking(curr+"(", left + 1, right)
                if right < left:
                    backtracking(curr+")", left, right+1)
        backtracking("", 0, 0)
        return rslt

    def generateParenthesis(self, n: int) -> List[str]:
        rslt = []
        def backtracking(curr, left, right):
            if left + right == 0:
                rslt.append(curr)
            else:
                if left > 0:
                    backtracking(curr+"(", left -1, right)
                if right > left:
                    backtracking(curr+")", left, right-1)
        backtracking("", n, n)
        return rslt
