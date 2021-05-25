class Solution:
    def longestValidParentheses(self, s: str) -> int:
        rslt = max(self.helper(s, '('), self.helper(s[::-1], ')'))
        return rslt

    def helper(self, s, check):
        left = right = rslt = 0
        for c in s:
            if c == check:
                left += 1
            else:
                right += 1

            if right > left:
                left, right = 0, 0
            elif right == left:
                rslt = max(rslt, 2*right)
        return rslt
