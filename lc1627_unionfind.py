class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        parent = list(range(n+1))
        size = [1]*(n+1)
        def find(p):
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        def union(p, q):
            rootp, rootq = find(p), find(q)
            if rootp == rootq: return
            if size[rootp] < size[rootq]:
                rootp, rootq = rootq, rootp
            parent[rootq] = rootp
            size[rootp] += size[rootq]
            return
        for i in range(n+1):
            if i > threshold and parent[i] == i:
                for j in range(2*i, n+1, i):
                    union(i, j)
        rslt = []
        for a, b in queries:
            rslt.append(find(a) == find(b))
        return rslt
