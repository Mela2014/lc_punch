class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dque, dp= collections.deque(), [0]*len(nums)
        for idx, num in enumerate(nums):
            while dque and idx - dque[0]  > k:
                dque.popleft()
            dp[idx] = max(num, dp[dque[0]]+num) if idx != 0 else num
            while dque and dp[dque[-1]] < dp[idx]:
                dque.pop()
            dque.append(idx)
        return max(dp)


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dque = collections.deque()
        for idx, num in enumerate(nums):
            if dque and idx - dque[0]  > k:
                dque.popleft()
            nums[idx] = max(num, nums[dque[0]]+num) if idx != 0 else num
            while dque and nums[dque[-1]] <= nums[idx]:
                dque.pop()
            dque.append(idx)
        return max(nums)
