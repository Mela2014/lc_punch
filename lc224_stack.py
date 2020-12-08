class Solution:
    def calculate(self, s: str) -> int:
        stk, last = ["("], False
        for c in s+")":
            if c == " ":
                continue
            if c.isdigit() and last:
                stk.append(stk.pop()+c)
            elif c.isdigit():
                stk.append(c)
                last = True
            elif c == ")":
                t_stk = []
                while stk[-1]!="(":
                    if stk[-1] == "-":
                        t_stk.append(-t_stk.pop())
                        stk.pop()
                    else:
                        t_stk.append(int(stk.pop()))
                stk.pop()
                stk.append(str(sum(t_stk)))
                last = False
            else:
                if c != "+":
                    stk.append(c)
                last = False

        return int(stk[0])
