class Solution:
    # def maxCoins(self, nums: List[int]) -> int:
    #     nnums = [1]+[num for num in nums if num > 0] + [1]
    #     n = len(nnums)
#         dp = [[0]*n  for _ in range(n)]
#         for l in range(2, n):
#             for left in range(0, n-l):
#                 right = left + l
#                 for mid in range(left+1, right):
#                     dp[left][right] = max(dp[left][right], nnums[left]*nnums[mid]*nnums[right]+dp[left][mid]+dp[mid][right])
#         return dp[0][n-1]
        # def dfs(left, right, memo = {}):
        #     if (left, right) in memo: return memo[(left, right)]
        #     rslt =  max([nnums[left]*nnums[mid]*nnums[right]+dfs(left, mid, memo)+dfs(mid, right, memo) for mid in range(left+1, right)] or [0] )
        #     memo[(left, right)] = rslt
        #     return rslt
        # return dfs(0, n-1)
    def maxCoins(self, nums: List[int]) -> int:
        nums = [x for x in nums if x != 0]
        def maxcoin(nums, memo = {}):
            if nums not in memo:
                first , last = nums[0], nums[-1]
                ans = max([maxcoin(nums[:k+1]) + maxcoin(nums[k:]) + first * nums[k] * last for k in range(1, len(nums)-1)] or [0] )
                memo[nums] = ans
            return memo[nums]

        return maxcoin(tuple([1] + nums + [1]))
