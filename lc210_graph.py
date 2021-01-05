class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, degree = collections.defaultdict(list), collections.defaultdict(int)
        for curr, pre in prerequisites:
            graph[pre].append(curr)
            degree[curr] += 1

        dque = collections.deque([crs for crs in range(numCourses) if degree[crs] == 0])
        rslt = []
        while dque:
            pre = dque.popleft()
            rslt.append(pre)
            for post in graph[pre]:
                degree[post] -= 1
                if degree[post] == 0:
                    dque.append(post)
        return rslt if len(rslt) == numCourses else []
