class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        left, holder, rslt = -1, {}, 0
        for right, c in enumerate(s):
            if c in holder:
                left = max(holder[c], left)
            rslt = max(rslt, right-left)
            holder[c] = right
        return rslt
