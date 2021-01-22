# dfs + memo
class Solution:
    def countVowelStrings(self, n: int) -> int:
        memo = {}
        def dfs(curr, rest):
            if (curr, rest) in memo:
                return memo[(curr, rest)]
            if curr == 1:
                return rest
            if rest == 1:
                return 1
            memo[(curr, rest)] = dfs(curr-1, rest)+dfs(curr, rest-1)
            return memo[(curr, rest)]
        return dfs(n, 5)
