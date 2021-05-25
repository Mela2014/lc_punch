class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.rslt = []
        self.helper(s, 0, 0, ('(', ')'))
        return self.rslt


    def helper(self, curr_s, s_check, s_modify, check):
        count = 0
        for i in range(s_check, len(curr_s)):
            count += (curr_s[i] == check[0]) - (curr_s[i] == check[1])
            if count >= 0: continue
            for j in range(s_modify, i+1):
                if curr_s[j] == check[1] and (j == s_modify or curr_s[j-1] != check[1]):
                    self.helper(curr_s[:j]+curr_s[j+1:], i, j, check)
            return
        curr_s = curr_s[::-1]
        if check[0] == '(':
            self.helper(curr_s, 0, 0, (')', '('))
        else:
            self.rslt.append(curr_s)
