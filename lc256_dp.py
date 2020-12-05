class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs: return 0
        dp = costs[0]
        for i in range(1, len(costs)):
            temp = [0]*3
            for j in range(3):
                temp[j] = costs[i][j] + min(dp[(j+1)%3], dp[j-1])
            dp = temp
        return min(dp)
