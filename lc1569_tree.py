class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def helper(nums):
            if not nums: return 1
            root = nums[0]
            left = [num for num in nums if num < root]
            right = [num for num in nums if num > root]
            l, r = len(left), len(right)
            return math.comb(l+r, l)*helper(left)*helper(right)
        return (helper(nums)-1)%(10**9+7)
