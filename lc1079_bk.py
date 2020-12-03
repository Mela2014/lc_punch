class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.rslt = 0
        temp = ''.join(sorted(list(tiles)))
        def backtracking(pref, cand):
            self.rslt +=1
            if not cand:
                return
            for i, c in enumerate(cand):
                if i !=0 and c == cand[i-1]:
                    continue
                backtracking(pref+c, cand[:i]+cand[i+1:])
            return
        backtracking('', temp)
        return self.rslt-1
