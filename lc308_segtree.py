class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.m, self.n = len(matrix), len(matrix[0])
        self.seg_tree = [[0]*(2*self.n) for _ in range(2*self.m)]
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])

    def update(self, row: int, col: int, val: int) -> None:
        m = row + self.m
        n = col + self.n
        self.seg_tree[m][n] = val
        while m > 0:
            self.seg_tree[m >> 1][n] = self.seg_tree[m][n]+self.seg_tree[m^1][n]
            t = n
            while t > 0:
                self.seg_tree[m][t >> 1] = self.seg_tree[m][t]+self.seg_tree[m][t^1]
                t >>= 1
            m >>= 1
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        rslt = 0
        r1 = self.m + row1
        r2 = self.m + row2
        while r1 <= r2:
            if r1&1:
                rslt += self.sumRange(r1, col1, col2)
                r1 += 1

            if r2&1 == 0:
                rslt += self.sumRange(r2, col1, col2)
                r2 -= 1
            r1 >>= 1
            r2 >>= 1
        return rslt

    def sumRange(self, row, col1, col2):
        rslt = 0
        l, r= self.n+col1, self.n+col2
        while l <= r:
            if l&1:
                rslt += self.seg_tree[row][l]
                l += 1
            if r&1 == 0:
                rslt += self.seg_tree[row][r]
                r -= 1
            l >>= 1
            r >>= 1
        return rslt
