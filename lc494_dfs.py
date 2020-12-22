class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memo = collections.defaultdict(int)
        def dfs(i, curr):
            if (i, curr) in memo:
                return memo[(i, curr)]
            if i == len(nums):
                return 1 if curr == S else 0
            memo[(i, curr)] = dfs(i+1, curr+nums[i])+dfs(i+1, curr-nums[i])
            return memo[(i, curr)]
        return dfs(0, 0)
