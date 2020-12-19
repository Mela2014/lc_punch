#dfs+memo
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def dfs(i_s, j_t):
            if (i_s, j_t) in memo:
                return memo[(i_s,j_t)]
            if j_t == len(t):
                temp = 1
            elif i_s == len(s):
                temp = 0
            elif s[i_s] == t[j_t]:
                temp = dfs(i_s+1, j_t+1)+dfs(i_s+1, j_t)
            else:
                temp =  dfs(i_s+1, j_t)
            memo[(i_s, j_t)] = temp
            return temp
        return dfs(0, 0)
# 1-d dp

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0]*(len(t)+1)
        dp[0] = 1
        for i in range(len(s)):
            temp = [1]*(len(t)+1)
            for j in range(len(t)):
                temp[j+1] = dp[j+1]
                if s[i] == t[j]:
                    temp[j+1] += dp[j]
            dp = temp
        return dp[-1]



class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        self.rslt = 0
        @lru_cache(None)
        def dfs(i_s, j_t):
            if j_t == len(t):
                return 1
            if i_s == len(s):
                return 0
            if s[i_s] == t[j_t]:
                return dfs(i_s+1, j_t+1)+dfs(i_s+1, j_t)
            else:
                return dfs(i_s+1, j_t)
        return dfs(0, 0)
