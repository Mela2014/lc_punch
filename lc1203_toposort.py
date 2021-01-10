class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        graph_i, graph_g = collections.defaultdict(list), collections.defaultdict(list)
        degree_i, degree_g = collections.defaultdict(int), collections.defaultdict(int)
        group_dict = collections.defaultdict(list)
        # Add to new group for item belongs to no group
        for i in range(n):
            if group[i] == -1: group[i] = m
            m += 1
            group_dict[group[i]].append(i)
        # Prepare for topo sort on groups then items
        for curr in range(n):
            for pre in beforeItems[curr]:
                if group[curr] == group[pre]:
                    graph_i[pre].append(curr)
                    degree_i[curr] += 1
                else:
                    graph_g[group[pre]].append(group[curr])
                    degree_g[group[curr]] += 1
        # order between group
        group_order, rslt = self.toposort(graph_g, degree_g, list(range(m))), []
        # order within group
        for i in group_order:
            if group_dict[i]:
                tt = self.toposort(graph_i, degree_i, group_dict[i])
                if len(tt) != len(group_dict[i]): return []
                rslt.extend(tt)
        return rslt

    def toposort(self, graph, degree, cands):
        dque = collections.deque([i for i in cands if degree[i] == 0])
        rslt = []
        while dque:
            pre = dque.popleft()
            rslt.append(pre)
            for post in graph[pre]:
                degree[post] -= 1
                if degree[post] == 0 and post in cands: dque.append(post)
        return rslt if len(rslt) == len(cands) else []
