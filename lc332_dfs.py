class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for start, end in tickets:
            graph[start].append(end)
        for key, val in graph.items():
            val.sort(reverse = True)
        rslt = []
        def dfs(start):
            while graph[start]:
                temp = graph[start].pop()
                dfs(temp)
            rslt.append(start)
        dfs("JFK")
        return rslt[::-1]
