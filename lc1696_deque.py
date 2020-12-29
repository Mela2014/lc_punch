class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dque, rslt, dp = collections.deque(), 0, [0]*len(nums)
        for idx, num in enumerate(nums):
            while dque and idx-dque[0] > k:
                dque.popleft()
            dp[idx] = num if idx == 0 else dp[dque[0]]+num
            while dque and dp[dque[-1]] <= dp[idx]:
                dque.pop()
            dque.append(idx)
        return dp[-1]

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dque = collections.deque()
        for idx, num in enumerate(nums):
            if idx == 0: dque.append(num)
            else:
                dque.append(dque[0]+num)
            while len(dque) > k:
                dque.popleft()
            while dque and dque[0] < dque[-1]:
                dque.popleft()
        return dque[-1]

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        rslt, dque = 0, collections.deque()
        for idx, num in enumerate(nums):
            if idx == 0: dque.append((idx, num))
            while dque and idx -  dque[0][0] > k:
                dque.popleft()
            rslt = dque[0][1]+num if idx != 0 else num
            while dque and dque[-1][1] <= rslt:
                dque.pop()
            dque.append((idx, rslt))
        return rslt
