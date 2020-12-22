class Solution:
    def getMoneyAmount(self, n: int) -> int:
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= j:
                return 0
            rslt = n**n
            for t in range(i, j+1):
                rslt = min(rslt, t+max(dfs(i, t-1), dfs(t+1, j)))
            memo[(i,j)] = rslt
            return rslt
        return dfs(1, n)
