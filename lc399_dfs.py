class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        grph = collections.defaultdict(dict)
        for (x, y), v in zip(equations, values):
            grph[x][y] = v
            grph[y][x] = 1/v

        def dfs(x, y, checked):
            if x == y:
                return 1
            checked.add(x)
            for z in grph[x]:
                if z in checked:
                    continue
                tmp = dfs(z, y, checked)
                if tmp > 0:
                    return tmp*grph[x][z]
            return -1
        return [dfs(x, y, set()) if x in grph and y in grph else -1 for x, y in queries]
