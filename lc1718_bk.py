class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        rslt = [0]*(2*n-1)
        mark = [0]*(n+1)
        def bk(i, cnt):
            if cnt == 0:
                return True
            if i >= 2*n-1:
                return False
            if rslt[i]:
                return bk(i+1, cnt)

            for num in range(n, 0, -1):
                left, right = i, i+num if num > 1 else i
                if not mark[num] and right < (2*n -1) and rslt[right] == 0:
                    mark[num] = 1
                    rslt[left] = rslt[right] = num
                    if bk(i+1, cnt-1): return True
                    mark[num] = 0
                    rslt[left] = rslt[right] = 0
            return False
        bk(0, n)
        return rslt
