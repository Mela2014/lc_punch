class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        def dfs(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            if left == right:
                return nums[left]
            memo[(left, right)] = max(nums[left]- dfs(left +1, right), nums[right]-dfs(left, right-1))
            return memo[(left, right)]
        return dfs(0, len(nums)-1) >= 0
