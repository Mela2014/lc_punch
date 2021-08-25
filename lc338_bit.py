class Solution:
    def countBits(self, n: int) -> List[int]:
        rslt = [0]
        while len(rslt) < n+1:
            for i in range(len(rslt)):
                rslt.append(rslt[i]+1)
                if len(rslt) > n: break
        return rslt[:n+1]
