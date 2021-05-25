class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        count_right, rslt = 0, 0
        for i, c in enumerate(s):
            if c == "(":
                count_right += 1
            else:
                count_right -= 1
                if s[i-1] == '(':
                    rslt += 2**count_right
        return rslt
