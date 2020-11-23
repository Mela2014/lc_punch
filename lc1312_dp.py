class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [1 if s[0] == s[-1] else 0]
        for i in range(1, n): dp.append(1 if s[i] == s[-1] else dp[i-1])
        for j in range(1, n):
            tdp = [max(dp[0], 1 if s[0] == s[n-j-1] else 0)]
            for i in range(1, n-j):
                temp = 1 if s[i] == s[n-j-1] else 0
                tdp.append(max(dp[i-1]+ temp, dp[i], tdp[i-1]))
            dp = tdp
        return n-dp[-1]
