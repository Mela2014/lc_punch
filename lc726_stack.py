class Solution:
    def countOfAtoms(self, expression: str) -> List[str]:
        stk, curr, atom, num = [], [], "", ""
        for c in expression+")":
            if c in "1234567890":
                num += c
            elif c in "abcdefghijklmnopqrstuvwxyz":
                atom += c
            elif atom:
                curr.append((atom, int(num) if num else 1))
                atom, num = "", ""
            elif num:
                t = int(num) if num else 1
                num = ""
                if stk:
                    temp = stk.pop()
                    curr = [(x, y*t) for (x, y) in temp]
                    curr = curr+stk.pop() if stk else curr
            if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                atom = c
            if c == ")" and curr:
                stk.append(curr)
                curr = []
            elif c == "(":
                stk.append(curr)
                curr = []
        rslt = {}
        for t in stk:
            for x,y in t:
                rslt[x] = rslt.get(x, 0)+y

        return "".join(key+str(rslt[key]) if rslt[key] > 1 else key for key in sorted(rslt.keys()))
