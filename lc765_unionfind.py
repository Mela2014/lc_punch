class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        parent = [x//2*2 for x in range(len(row))]
        size = [1]*len(row)
        def find(p):
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(p, q):
            rootp, rootq = find(p), find(q)
            if rootp == rootq: return False
            if size[rootp] < size[rootq]:
                rootp, rootq = rootq, rootp
            parent[rootq] = rootp
            size[rootp] += size[rootq]
            return True
        rslt = 0
        for i in range(len(row)//2):
            if union(row[i*2], row[i*2+1]):
                rslt += 1
        return rslt
