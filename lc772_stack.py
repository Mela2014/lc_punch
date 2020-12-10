class Solution:
    def calculate(self, s: str) -> int:
        stk, last = ["("], ""
        for c in s+")":
            if c == " ": continue
            if c.isdigit():
                last += c if last else c
            elif c == "(":
                stk.append(c)
            else:
                op = stk.pop()
                if op == "*":
                    stk.append(int(stk.pop())*int(last))
                elif op == "/":
                    stk.append(int(int(stk.pop())/int(last)))
                elif op == "-":
                    stk.append(-int(last))
                else:
                    stk.append(op)
                    stk.append(int(last))
                last = ""
                if c == ")":
                    y = 0
                    while stk[-1] !="(":
                        y += stk.pop()
                    stk.pop()
                    last = str(y)
                elif c != "+":
                    stk.append(c)
        return int(last)
