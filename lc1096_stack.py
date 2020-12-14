class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stk, pre, curr = [], [], [""]
        for c in expression:
            if c == ",":
                pre += curr
                curr = [""]
            elif c == "{":
                stk.append(pre)
                stk.append(curr)
                pre, curr = [], [""]
            elif c == "}":
                p_curr = stk.pop()
                p_pre = stk.pop()
                curr = [s+k for k in pre+curr for s in p_curr]
                pre = p_pre
            else:
                curr = [s+c for s in curr]
        return sorted(set(pre+curr))
