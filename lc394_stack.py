class Solution:
    def decodeString(self, s: str) -> str:
        stack, digit, currs, rslt = [], "", "", ""
        for c in s:
            if c.isalpha():
                currs += c
            elif c.isdigit():
                digit += c
            elif c == "[":
                if currs:
                    stack.append(currs)
                stack.append(digit)
                digit, currs= "", ""
            elif c == "]":
                lastc = int(stack.pop()) if stack and stack[-1].isdigit() else 1
                currs = lastc*currs
                while stack and stack[-1].isalpha():
                    currs = stack.pop()+currs
            if not stack:
                rslt += currs
                currs = ""
        return rslt
