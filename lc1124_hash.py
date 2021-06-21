class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        maps = {}
        curr, rslt = 0, 0
        for i, hour in enumerate(hours):
            curr = curr + 1 if hour > 8 else curr-1
            if curr > 0:
                rslt = i + 1
            if curr not in maps: maps[curr] = i
            if curr-1 in maps:
                rslt = max(rslt, i-maps[curr-1])
        return rslt
        
