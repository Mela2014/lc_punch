class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        memo, word_set = {}, set(words)
        def dfs(word):
            if len(word) == 1: return 1
            if word in memo: return memo[word]
            rslt = 0
            for i in range(len(word)):
                if word[:i] + word[i+1:] in word_set:
                    rslt = max(rslt, dfs(word[:i] + word[i+1:]))
            memo[word] = rslt + 1
            return rslt + 1
        rslt = 0
        for word in words[::-1]:
            rslt = max(rslt, dfs(word))
        return rslt
