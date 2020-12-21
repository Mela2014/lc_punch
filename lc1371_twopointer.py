class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mask = {"a":1, "e":2, "i":4, "o":8, "u":16}
        d, n, res = {0:-1}, 0, 0
        for i, c in enumerate(s):
            if c in mask:
                n ^= mask[c]
            if n not in d:
                d[n] = i
            else:
                res = max(res, i-d[n])
        return res
