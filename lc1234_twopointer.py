class Solution:
    def balancedString(self, s: str) -> int:
        count = collections.Counter(s)
        extra = {}
        n = len(s)
        a = n//4
        for key in count:
            if count[key] > a:
                extra[key] = count[key]-a
        if not extra: return 0
        l, rslt = 0, len(s)
        for r in range(n):
            if s[r] in extra:
                extra[s[r]]-=1
            while max(extra.values()) <= 0:
                rslt = min(rslt, r-l+1)
                if s[l] in extra:
                    extra[s[l]] += 1
                l += 1
        return rslt
