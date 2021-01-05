class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        temp = {}
        for i, c in enumerate(S):
            temp[c] = i
        left, right, rslt = 0, 0, []
        for i, c in enumerate(S):
            right = max(right, temp[c])
            if i == right:
                rslt.append(right-left+1)
                left = right+1
        return rslt
