class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        isPre = collections.defaultdict(set)
        graph, degree = collections.defaultdict(list), collections.defaultdict(int)
        for pre, curr in prerequisites:
            graph[pre].append(curr)
            isPre[curr].add(pre)
            degree[curr] += 1
            degree[pre] += 0

        dque = collections.deque([v for v in degree if degree[v] == 0])
        while dque:
            temp = dque.popleft()
            for post in graph[temp]:
                isPre[post] |= isPre[temp]
                degree[post] -= 1
                if degree[post] == 0:
                    dque.append(post)
        return [x in isPre[y] for x, y in queries]
