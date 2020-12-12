class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        stk, last, curr = [], "", None
        for c in s:
            if c in ",]":
                if last:
                    stk[-1].add(NestedInteger(int(last)))
                    last = ""
                if c == "]":
                    rslt = stk.pop()
            elif c == "[":
                temp = NestedInteger()
                if stk:
                    stk[-1].add(temp)
                stk.append(temp)
            else:
                last += c
        if not stk and last:
            return NestedInteger(int(last))
        return rslt
