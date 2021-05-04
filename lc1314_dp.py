class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        nrow, ncol = len(mat), len(mat[0])
        presum = [[0]*(ncol+1) for _ in range(nrow+1)]
        for i in range(nrow):
            for j in range(ncol):
                presum[i+1][j+1] = presum[i][j+1]+ presum[i+1][j] + mat[i][j] - presum[i][j]
        rslt = [[0]*ncol for _ in range(nrow)]
        for i in range(nrow):
            for j in range(ncol):
                r1, r2 = max(0, i-k), min(nrow, i+k+1)
                c1, c2 = max(0, j-k), min(ncol, j+k+1)
                rslt[i][j] = presum[r2][c2] - presum[r2][c1]-presum[r1][c2]+ presum[r1][c1]
        return rslt
