class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        for start, end in connections:
            graph[start].append(end)
            graph[end].append(start)
        visited, rslt = {}, []
        def dfs(cur, pre, d):
            visited[cur] = d
            for end in graph[cur]:
                if end == pre:
                    continue
                if end not in visited:
                    visited[cur] = min(visited[cur], dfs(end, cur, d+1))
                else:
                    visited[cur] = min(visited[cur], visited[end])
            if visited[cur] == d and pre != -1:
                rslt.append([pre, cur])
            return visited[cur]
        dfs(0, -1, 0)
        return rslt
