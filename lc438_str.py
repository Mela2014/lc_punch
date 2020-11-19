class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        counter_p, counter_s, cnt, rslt = collections.Counter(p), {}, 0, []
        
        for i, c in enumerate(s):
            if c not in counter_p:
                counter_s = {}
                cnt = 0
            elif cnt < len(p):
                counter_s[c] = counter_s.get(c, 0) +1
                cnt += 1
            else:
                counter_s[c] = counter_s.get(c, 0) + 1
                counter_s[s[i-len(p)]] -= 1
            if counter_s == counter_p:
                    rslt.append(i-len(p)+1)
        return rslt