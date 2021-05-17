class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        bdry = {}
        for i, c in enumerate(s):
            if c not in bdry:
                bdry[c] = [i, i]
            else:
                bdry[c][1] = i
        for c in set(s):
            left, right = bdry[c]
            l, r = left, right
            while True:
                for oc in set(s[left:right+1]):
                    l = min(l, bdry[oc][0])
                    r = max(r, bdry[oc][1])
                if [left, right] == [l, r]: break
                left, right = l, r
            bdry[c] = [l, r]

        intervals = sorted(bdry.values(), key = lambda x: x[1])
        rslt, last = [], -1
        for st, ed in intervals:
            if st > last:
                rslt.append(s[st:ed+1])
                last = ed
        return rslt
