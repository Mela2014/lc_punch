class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def dfs(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            if left == right:
                return piles[left]
            memo[(left, right)] = max(piles[left]-dfs(left+1, right), piles[right]-dfs(left, right-1))
            return memo[(left, right)]
        return dfs(0, len(piles)-1) > 0
