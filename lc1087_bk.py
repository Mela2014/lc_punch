class Solution:
    def expand(self, S: str) -> List[str]:
        rslt = []
        def backtracking(prefix, remain):
            if not remain:
                rslt.append(prefix)
                return
            if remain[0] == '{':
                temp, cans = 0, []
                for i, c in enumerate(remain):
                    if c == '}':
                        temp = i
                        break
                    if c in ('{', ','):
                        continue
                    cans.append(c)
                for can in cans:
                    backtracking(prefix+can, remain[i+1:])
            else:
                backtracking(prefix+remain[0], remain[1:])
        backtracking("", S)
        return sorted(rslt)
