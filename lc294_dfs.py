class Solution:
    def canWin(self, s: str) -> bool:
        memo = {}
        def dfs(s):
            if s in memo:
                return memo[s]
            for i in range(len(s)-1):
                if s[i] == "+" and s[i+1] == "+" and not dfs(s[:i]+"-"+s[i+2:]):
                    memo[s] = True
                    return True
            memo[s] = False
        return dfs(s)
