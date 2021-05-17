class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        presum = [0]*(n+1)
        for i in range(n): presum[i+1] = presum[i] + nums[i]
        stack, rslt = [], 0
        for i, h in enumerate(nums+[0]):
            start = i
            while stack and stack[-1][1] >= h:
                start, mh = stack.pop()
                rslt = max(rslt, (presum[i] - presum[start])*mh)
            stack.append((start, h))
        return rslt %(10**9 + 7)
