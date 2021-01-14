class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        r, c= len(board), len(board[0])
        uf, edge = UF(r*c+1), r*c
        for i in range(r):
            if board[i][0] == "O": uf.union(i*c, edge)
            if board[i][c-1] == "O": uf.union(i*c + c-1, edge)
        for j in range(c):
            if board[0][j] == "O": uf.union(j, edge)
            if board[r-1][j] == "O": uf.union(c*(r-1)+j, edge)
        for i in range(1, r-1):
            for j in range(1, c-1):
                if board[i][j] == 'O':
                    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        if board[i+x][j+y] == "O":
                            uf.union(i*c+j, (i+x)*c+j+y)
        for i in range(1, r-1):
            for j in range(1, c-1):
                if board[i][j] == "O" and uf.find(i*c+j) != uf.find(edge):
                    board[i][j] = 'X'


class UF:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq: return
        if self.size[rootp] > self.size[rootq]:
            rootp, rootq = rootq, rootp
        self.parent[rootp] = rootq
        self.size[rootq] += self.size[rootp]

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
