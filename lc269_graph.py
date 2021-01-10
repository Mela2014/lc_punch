class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph, degree = collections.defaultdict(list), {x:0 for word in words for x in word}
        for i, word in enumerate(words[:-1]):
            for j, c in enumerate(word):
                if j >= len(words[i+1]):
                    return ""
                if c != words[i+1][j]:
                    graph[c].append(words[i+1][j])
                    degree[words[i+1][j]] += 1
                    break
        dque, rslt = collections.deque([a for a in degree if degree[a] == 0]), []
        while dque:
            temp = dque.popleft()
            rslt.append(temp)
            for end in graph[temp]:
                degree[end] -= 1
                if degree[end] == 0:
                    dque.append(end)
        return "".join(rslt) if len(rslt) == len(degree) else ""
