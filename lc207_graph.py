class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites: return True
        graph = collections.defaultdict(list)
        visited = [0]*numCourses
        for crs, pre in prerequisites:
            graph[crs].append(pre)

        def dfs(crs):
            # in cycle
            if visited[crs] == 1:
                return False
            # not in cycle
            if visited[crs] == 2:
                return True
            # new node: assume in cycle until approve not
            visited[crs] = 1
            if crs in graph:
                for pre in graph[crs]:
                    if not dfs(pre): return False
            visited[crs] = 2
            return True

        for crs in graph:
            if not dfs(crs): return False
        return True


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites: return True
        graph, degree = collections.defaultdict(list), collections.defaultdict(int)
        for crs, pre in prerequisites:
            graph[pre].append(crs)
            degree[crs] += 1
        dque = collections.deque()
        for i in range(numCourses):
            if degree[i] == 0: dque.append(i)
        count = 0
        while dque:
            curr = dque.popleft()
            count += 1
            for post in graph[curr]:
                degree[post] -= 1
                if degree[post] == 0:
                    dque.append(post)
        return count == numCourses
