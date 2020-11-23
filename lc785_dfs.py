class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        set_map = {}
        def dfs(node):
            for snode in graph[node]:
                if snode not in set_map:
                    set_map[snode] = 1 - set_map[node]
                    if not dfs(snode): return False
                elif set_map[node] == set_map[snode]:
                    return False
            return True

        for i in range(len(graph)):
            if graph[i] and i not in set_map:
                set_map[i] = 1
                if not dfs(i): return False
        return True
