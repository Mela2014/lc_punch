class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        dque = collections.deque()
        visited, mark = {}, 0
        for i in range(len(graph)):
            if i not in visited:
                dque.append((i, mark))
            while dque:
                cur, mark = dque.popleft()
                mark = (mark+1)%2
                for post in graph[cur]:
                    if post in visited and visited[post] != mark:
                        return False
                    elif post not in visited:
                        visited[post] = mark
                        dque.append((post, mark))
        return True
