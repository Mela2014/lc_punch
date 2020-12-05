class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        rslt, stk = [0]*n, []
        for log in logs:
            idx, op, time = log.split(":")
            if op == "end":
                rslt[int(idx)] += int(time)-stk[-1][1]+1
                stk.pop()
                if stk: stk[-1][1] = int(time)+1
                continue
            if stk:
                rslt[int(stk[-1][0])] += int(time)-stk[-1][1]
            stk.append([idx, int(time)])
        return rslt
