class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        richer_map = collections.defaultdict(set)
        for x, y in richer:
            richer_map[y].add(x)
        memo = {}
        def dfs(x):
            if x in memo:
                return memo[x]
            if not richer_map[x]:
                return x
            curr, rslt = quiet[x], x
            for t in richer_map[x]:
                temp = dfs(t)
                if quiet[temp] < curr:
                    curr = quiet[temp]
                    rslt = temp
            memo[x] = rslt
            return rslt
        return [dfs(x) for x in range(len(quiet))]
