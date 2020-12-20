class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(target+1):
            for num in nums:
                if i-num >= 0:
                    dp[i] = dp[i] + dp[i-num]
        return dp[-1]
            
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {0:1}
        def dfs(t):
            if t in memo:
                return memo[t]
            rslt = 0
            for num in nums:
                if num <= t:
                    rslt += dfs(t-num)
            memo[t] = rslt
            return rslt
        return dfs(target)
