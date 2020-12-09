class Solution:
    def calculate(self, s: str) -> int:
        stk, last, op = [], "", None
        for c in s+"+":
            if c == " ": continue
            if c.isdigit():
                last = last+c if last else c
            else:
                if op == "*":
                    stk.pop()
                    stk.append(int(stk.pop())*int(last))
                elif op == "/":
                    stk.pop()
                    stk.append(int(stk.pop())//int(last))
                else:
                    stk.append(last)
                stk.append(c)
                op = c
                last = ""
        rslt, last = 0, 0

        while stk:
            temp = stk.pop()
            if temp == "-":
                rslt -= 2*last
            elif temp != "+":
                last = int(temp)
                rslt += last

        return rslt
