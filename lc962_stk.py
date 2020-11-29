class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        stk = []
        for i, num in enumerate(A):
            if not stk or A[stk[-1]] > num:
                stk.append(i)
        rslt = 0
        for i, num in enumerate(A[::-1]):
            while stk and A[stk[-1]] <= num:
                rslt = max(rslt, len(A)-1-i-stk.pop())
        return rslt
