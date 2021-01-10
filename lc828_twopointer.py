class Solution:
    def uniqueLetterString(self, s: str) -> int:
        index, rslt = {c:[-1, -1] for c in string.ascii_uppercase}, 0
        for i, c in enumerate(s):
            pre, last = index[c]
            rslt += (i-last)*(last-pre)
            index[c] = [last, i]
        n = len(s)
        for c in index:
            rslt += (n-index[c][1])*(index[c][1]-index[c][0])
        return rslt%(10**9+7)
