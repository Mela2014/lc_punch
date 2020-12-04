class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num): return "0"
        stk, temp= [], k
        for i, c in enumerate(num):
            while stk and temp > 0 and stk[-1] > c:
                stk.pop()
                temp -= 1
            if temp == 0:
                return str(int("".join(stk)+num[i:]))
            stk.append(c)
        return str(int("".join(stk[:len(num)-k])))
