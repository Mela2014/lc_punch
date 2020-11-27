class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        rslt = []
        def backtracking(word, pattern):
            if not pattern:
                for c in word:
                    if c.isupper():
                        return False
                return True
            for i, c in enumerate(word):
                if c == pattern[0]:
                    return backtracking(word[i+1:], pattern[1:])
                if c.isupper():
                    return False
            return False
        for query in queries:
            rslt.append(backtracking(query, pattern))
        return rslt
