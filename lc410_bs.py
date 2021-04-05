class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = 0, 0
        n = len(nums)
        for i in range(n):
            right += nums[i]
            if left < nums[i]: left = nums[i]
        rslt = right
        while left <= right:
            mid = (left + right)//2
            total = 0
            count = 0
            # check if is a viable mid
            for i in range(n):
                if total + nums[i] > mid:
                    count += 1
                    total = nums[i]
                else:
                    total += nums[i]
            if count < m:
                rslt = min(rslt, mid)
                right = mid - 1
            else:
                left = mid + 1
        return rslt
                    
