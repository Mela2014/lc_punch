# BK
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordmap = collections.Counter(words)
        n, m, l = len(words), len(words[0]), len(s)
        lsub = n*m
        if lsub == l and "".join(words) == s: return [0]
        rslt = []
        def backtracking(right, checked):
            if checked == lsub:
                rslt.append(right-lsub)
            elif right < l:
                temp = s[right:right+m]
                if temp in wordmap and wordmap[temp] > 0:
                    wordmap[temp] -= 1
                    backtracking(right+m, checked+m)
                    wordmap[temp] += 1
        for i in range(l):
            backtracking(i, 0)
        return rslt
