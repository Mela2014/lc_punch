class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T: return T
        stk, rslt = [], [0]*len(T)
        for i, t in enumerate(T):
            while stk and t > T[stk[-1]]:
                pre_id = stk.pop()
                rslt[pre_id] = i - pre_id
            stk.append(i)
        return rslt
