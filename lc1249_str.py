class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, c in enumerate(s+'*'):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack and s[stack[-1]] == '(': stack.pop()
                else: stack.append(i)
        stack = set(stack)
        return "".join(c for i, c in enumerate(s) if c not in ['(', ')'] or i not in stack)
