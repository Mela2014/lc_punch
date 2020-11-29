class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        rslt = []
        def backtracking(i):
            if i >= low and i <= high:
                rslt.append(i)
            if i > high:
                return
            if i != 0 and i%10 < 9:
                backtracking(i*10 + i%10+1)
            if i != 0 and i%10 > 0:
                backtracking(i*10 + i%10-1)
            return
        for j in range(10):
            backtracking(j)
        return sorted(rslt)
