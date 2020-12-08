# BK
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse = True)
        self.rslt = float("inf")
        def backtracking(amount, i, val):
            if amount == 0:
                self.rslt = min(self.rslt, val)
                return
            if i>= len(coins) or amount < 0 or val + amount //coins[i] +1 > self.rslt:
                return
            temp = amount //coins[i]
            for j in range(temp, -1, -1):
                backtracking(amount-coins[i]*j, i+1, val+j)

        backtracking(amount, 0, 0)
        return self.rslt if self.rslt < float("inf") else -1

# DP
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")]*(amount+1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin] + 1)
        return dp[-1] if dp[amount] < float("inf") else -1
