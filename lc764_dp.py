class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        mines = {tuple(x) for x in mines}
        dp = [[[0,0] for _ in range(N+2)] for _ in range(N+2)]
             # left, above, right, below
        # left, above
        for i in range(N):
            for j in range(N):
                if (i, j) not in mines:
                    dp[i+1][j+1][0] = dp[i+1][j][0] + 1
                    dp[i+1][j+1][1] = dp[i][j+1][1] + 1
        # right, below
        rslt = 0
        for i in range(N, 0, -1):
            for j in range(N, 0, -1):
                if (i-1, j-1) not in mines:
                    dp[i][j][0] = min(dp[i][j][0], dp[i][j+1][0] + 1)
                    dp[i][j][1] = min(dp[i][j][1], dp[i+1][j][1] + 1)
                rslt = max(rslt, min(dp[i][j]))

        return rslt
