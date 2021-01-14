class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        # sort the connections by cost
        connections.sort(key = lambda x: x[2])
        parent = list(range(N+1))
        size = [1]*len(N+1)
        def find(p):
            while p!= parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        def union(p, q, cost):
            rootp, rootq = find(p), find(q)
            if rootp == rootq: return -1
            if size[rootp] < size[rootq]: rootp, rootq = rootq, rootp
            parent[rootq] = rootp
            size[rootp] += size[rootq]
            return cost
        rslt, count = 0, 0
        for x, y, cost in connections:
            temp = union(x, y, cost)
            if cost >= 0:
                rslt += cost
                count += 1
        return rslt if count == N-1 else -1


class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        # sort the connections by cost
        connections.sort(key = lambda x: x[2])
        parent = list(range(N+1))
        size = [1]*(N+1)
        def find(p):
            while p!= parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        def union(p, q, cost):
            rootp, rootq = find(p), find(q)
            if rootp == rootq: return -1
            if size[rootp] < size[rootq]: rootp, rootq = rootq, rootp
            parent[rootq] = rootp
            size[rootp] += size[rootq]
            return cost
        rslt, count = 0, 0
        for x, y, cost in connections:
            temp = union(x, y, cost)
            if temp >= 0:
                rslt += temp
                count += 1
        return rslt if count == N-1 else -1


class UF:
            def __init__(self, n): self.p = list(range(n))
            def union(self, x, y): self.p[self.find(x)] = self.find(y)
            def find(self, x):
                if x != self.p[x]: self.p[x] = self.find(self.p[x])
                return self.p[x]
