class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        dque_max, dque_min, l= collections.deque(), collections.deque(), 0
        for num in nums:
            while dque_max and dque_max[-1] < num: dque_max.pop()
            while dque_min and dque_min[-1] > num: dque_min.pop()
            dque_max.append(num)
            dque_min.append(num)
            if dque_max and dque_min and dque_max[0] -  dque_min[0] > limit:
                if dque_max[0] == nums[l]: dque_max.popleft()
                if dque_min[0] == nums[l]: dque_min.popleft()
                l += 1
            # print(dque_max, dque_min, l)
        return len(nums)-l
