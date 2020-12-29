class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        rslt, holder = [], collections.deque()
        for idx, num in enumerate(nums):
            while holder and nums[holder[-1]] < num:
                holder.pop()
            holder.append(idx)
            if holder[0] <= idx-k:
                holder.popleft()
            if idx >= k-1:
                rslt.append(nums[holder[0]])
        return rslt
