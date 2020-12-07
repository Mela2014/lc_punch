class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        for p in path.split("/"):
            if p in ("", "."):
                continue
            if p != "..":
                stk.append(p)
            elif stk:
                stk.pop()
        return '/'+'/'.join(stk)
