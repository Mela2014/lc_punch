class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [False]*n
        dp[0] = True
        cand_steps =collections.defaultdict(set)
        cand_steps[0] = {1}
        for i in range(1, n):
            for j in range(i):
                need_step = stones[i] - stones[j]
                if dp[j] and need_step in cand_steps[j]:
                    dp[i] = True
                    cand_steps[i]|= {need_step, need_step+1, need_step-1}
        return dp[-1]

    def canCross(self, stones):
        maps = {x: set() for x in stones}
        maps[0].add(0)
        for x in stones[:-1]:
            for j in maps[x]:
                for k in range(max(1, j-1), j+2):
                    if x + k in maps:
                        maps[x+k].add(k)
        return bool(maps[stones[-1]])
