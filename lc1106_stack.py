class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk_op, stk_or, ops = [], [], {"t":True, "f":False, "|": lambda x, y: x or y, "&":lambda x, y : x and y, "!":lambda x: not x, "(":"("}
        for c in expression:
            if c == ",": continue
            if c in ("t", "f", "("):
                stk_op.append(ops[c])
            elif c in ("!", "|", "&"):
                stk_or.append(c)

            if c == ")":
                opr = stk_or.pop()
                rslt = True if opr == "&" else False
                if opr == "!":
                    rslt = ops[opr](stk_op.pop())
                else:
                    while stk_op[-1] != "(":
                        rslt = ops[opr](rslt, stk_op.pop())
                stk_op.pop()
                stk_op.append(rslt)
        return stk_op[0]
