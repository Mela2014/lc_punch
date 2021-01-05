class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        graph, degree = collections.defaultdict(list), collections.defaultdict(int)
        for seq in seqs:
            for i, x in enumerate(seq):
                if i != len(seq)-1:
                    graph[x].append(seq[i+1])
                    degree[seq[i+1]]+= 1
                degree[x] += 0
        dque = collections.deque([x for x in degree if degree[x] == 0])
        temp = []
        while dque:
            if len(dque) != 1: return False
            t = dque.popleft()
            temp.append(t)
            for end in graph[t]:
                degree[end] -= 1
                if degree[end] == 0:
                    dque.append(end)
        return temp == org and sum(degree.values()) == 0
