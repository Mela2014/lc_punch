class Solution:
    def longestAwesome(self, s: str) -> int:
        rslt, curr = 0, 0
        seen =  {0:-1}
        for i, c in enumerate(s):
            curr ^= 1 << int(c)
            if curr not in seen:
                seen[curr] = i
            rslt = max(rslt, i-seen[curr])
            for j in range(10):
                if curr^(1 << j) in seen:
                    rslt = max(rslt, i-seen[curr^(1<<j)])
        return rslt
