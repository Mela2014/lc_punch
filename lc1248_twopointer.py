class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left, rslt, last = 0, 0, 0
        for right, num in enumerate(nums):
            if num%2 == 1:
                k -= 1
                last = 0
            while k == 0:
                last += 1
                k += nums[left]%2
                left += 1
            rslt += last
        return rslt



class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left, rslt, count = 0, 0, 0
        for right, num in enumerate(nums):
            count += num%2
            while count > k:
                count -= nums[left]%2
                left += 1
            temp = left
            while count == k:
                count -= nums[temp] % 2
                rslt += 1
                temp += 1
            if temp > left:
                count += 1
        return rslt
