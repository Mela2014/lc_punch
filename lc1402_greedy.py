class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        curr = 0
        rslt = 0
        for val in satisfaction:
            curr += val
            if curr < 0:
                break
            rslt += curr

        return rslt
        
