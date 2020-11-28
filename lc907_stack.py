class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        modulo = 10**9 + 7
        stk, rslt, remain = [], 0, 0
        for i, num in enumerate(arr):
            count = 1
            while stk and stk[-1][0] >= num:
                tnum, tcount = stk.pop()
                count += tcount
                remain -= tnum*tcount
            remain += count*num
            rslt += remain
            stk.append((num, count))
        return rslt%modulo
