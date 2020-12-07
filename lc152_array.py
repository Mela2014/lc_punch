class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = None
        for num in nums:
            if dp is None:
                dp = [num]*3
                continue
            dp[0], dp[1] = max(num, dp[0]*num, dp[1]*num), min(num, dp[1]*num, dp[0]*num)
            dp[2] = max(dp[2], dp[0])
        return dp[2]
