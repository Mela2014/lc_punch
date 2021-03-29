class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left, right = k, k
        rslt = nums[k]
        tempmin = nums[k]
        n = len(nums)
        while left > 0 or right < n-1:
            if left == 0 or (right < n-1 and nums[left-1] < nums[right+1]):
                right += 1
                tempmin = min(nums[right], tempmin)
            elif right == n-1 or (left > 0 and nums[left-1] > nums[right+1]):
                left -= 1
                tempmin = min(nums[left], tempmin)
            else:
                left -= 1
                right += 1
                tempmin = min(nums[right], tempmin)

            rslt = max(rslt, (right-left+1)*tempmin)
        return rslt

                
