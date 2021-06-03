class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        cp, cn =0, 0
        rslt = 0
        for num in nums:
            if num > 0:
                cp, cn = cp+1, cn+1 if cn else 0
            elif num < 0:
                cp, cn = cn+1 if cn else 0, cp+1
            else:
                cp, cn = 0, 0
            rslt = max(rslt, cp)
        return rslt
        
