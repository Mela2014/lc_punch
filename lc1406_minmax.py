class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(stoneValue):
                return 0
            rslt = float("-inf")
            for j in range(3):
                if i+j+1 > len(stoneValue): break
                rslt = max(rslt, sum(stoneValue[i:i+j+1])-dfs(i+j+1))
            memo[i] = rslt
            return rslt
        temp = dfs(0)
        return "Tie" if temp == 0 else "Alice" if temp > 0 else "Bob"
