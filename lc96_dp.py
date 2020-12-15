class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        for total in range(1, n+1):
            for left in range(1, total+1):
                dp[total] += dp[left-1]*dp[total-left]
        return dp[-1]
