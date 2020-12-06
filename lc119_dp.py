class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        dp = [1]
        for j in range(1, rowIndex+1):
            temp = [1]*(j+1)
            for i in range(1, j):
                temp[i] = dp[i-1] + dp[i]
            dp = temp
        return dp
