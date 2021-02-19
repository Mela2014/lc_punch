class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not wordDict: return []
        n, wordDict, ml = len(s), set(wordDict), len(max(wordDict, key = len))
        @lru_cache(None)
        def dfs(i):
            if i == n:
                return [[]]
            rslt = []
            for j in range(i, n):
                if j-i < ml and s[i:j+1] in wordDict:
                    temp = dfs(j+1)
                    for t in temp:
                        rslt.append([s[i:j+1]]+t)
            return rslt
        temp = dfs(0)
        return [" ".join(t) for t in temp]
