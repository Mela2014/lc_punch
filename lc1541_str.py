class Solution:
    def minInsertions(self, s: str) -> int:
        bal, rslt = 0, 0
        for c in s:
            if c == "(":
                if bal % 2 == 1:
                    rslt += 1
                    bal -= 1
                bal += 2
            else:
                bal -= 1
                if bal < 0:
                    rslt += 1
                    bal += 2
        return rslt + bal
