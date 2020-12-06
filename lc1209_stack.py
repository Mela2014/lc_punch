class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        for c in s:
            if stk and  c == stk[-1][0]:
                stk[-1][1] +=1
                if stk[-1][1] == k:
                    stk.pop()
            else:
                stk.append([c, 1])
        return "".join([x[0]*x[1] for x in stk])
