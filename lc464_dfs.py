class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @lru_cache(None)
        def dfs(cands, target):
            if not cands:
                return False
            if cands[-1] >= target:
                return True

            for i, cand in enumerate(cands):
                if not dfs(cands[:i]+cands[i+1:], target-cand):
                    return True
            return False
        if maxChoosableInteger*(maxChoosableInteger+1)//2 < desiredTotal: return False
        return dfs(tuple(range(1, maxChoosableInteger+1)), desiredTotal)
