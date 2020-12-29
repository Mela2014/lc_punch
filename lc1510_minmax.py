class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        memo = {}
        def dfs(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return False
            for i in range(1, int(math.sqrt(n))+1):
                if i*i <= n and not dfs(n-i*i):
                    memo[n] = True
                    return True
            memo[n] = False
            return False
        return dfs(n)
