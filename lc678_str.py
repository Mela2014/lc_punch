class Solution:
    def checkValidString(self, s: str) -> bool:
        countl = 0
        for c in s:
            countl += 1 if c in ("(", "*") else -1
            if countl < 0: return False
        countr = 0
        for c in s[::-1]:
            countr += 1 if c in (")", "*") else -1
            if countr < 0: return False
        return True
    def checkValidString(self, s:str) -> bool:
        low, hi= 0, 0
        for c in s:
            low += 1 if c == '(' else -1
            hi += 1 if c in ('(', '*') else -1
            low = max(0, low)
            if hi < 0: return False
        return low == 0
        
