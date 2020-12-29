class Solution:
    def divisorGame(self, N: int) -> bool:
        memo = {}
        def dfs(n):
            if n in memo: return memo[n]
            if n == 1: return False
            rslt = False
            for i in range(1, n):
                if n%i == 0 and not dfs(n-i):
                    memo[n] = True
                    return True
            memo[n] = False
            return False
        return dfs(N)

class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0
