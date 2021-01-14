class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        for x, y in edges:
            uf.union(x, y)
        return uf.getsize()


class UF:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
        self.count = n
    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:return
        if self.size[rootp] < self.size[rootq]:
            rootp, rootq = rootq, rootp
        self.parent[rootq] = rootp
        self.size[rootp] += self.size[rootq]
        self.count -= 1
        return
    def find(self, p):
        while self.parent[p] != p:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    def getsize(self):
        return self.count
