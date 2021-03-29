class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1]*n
    def find(self, p):
        while self.parents[p] != p:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p
    def union(self, p, q):
        pp, pq = self.find(p), self.find(q)
        if pp == pq: return True
        if self.size[pp] < self.size[pq]:
            pp, pq = pq, pp
        self.parents[pq] = pp
        self.size[pp] += self.size[pq]
        return False

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        cand1, cand2, parents = None, None, {}
        for u, v in edges:
            if v in parents:
                cand1 = [parents[v], v]
                cand2 = [u, v]
                break
            parents[v] = u

        dsu = DSU(len(edges)+1)
        for u, v in edges:
            if cand2 == [u, v]: continue
            if dsu.union(u, v):
                if cand1: return cand1
                return [u, v]
        return cand2
