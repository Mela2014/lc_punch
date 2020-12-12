class Solution:
    def expand(self, S: str) -> List[str]:
        rslt, curr, append = [""], [],  False
        for c in S:
            if c == ",": continue
            if c == "{": append = True
            elif c == "}":
                append = False
                temp = []
                while curr:
                    t = curr.pop()
                    temp += [x+t for x in rslt]
                rslt = temp
            elif append:
                curr.append(c)
            else:
                rslt = [x+c for x in rslt]
        return sorted(rslt)
