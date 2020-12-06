class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rslt = []
        for i in range(numRows):
            temp = [1]*(i+1)
            for j in range(1, i):
                temp[j] = rslt[i-1][j-1]+rslt[i-1][j]
            rslt.append(temp)
        return rslt
