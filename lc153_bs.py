class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if left == right or nums[left] < nums[right]: return nums[left]
        while left <= right:
            mid = (left + right)// 2
            if nums[mid] > nums[mid + 1]: return nums[mid+1]
            if nums[mid] < nums[-1]:
                right = mid-1
            else:
                left = mid + 1
        return nums[left]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] <= nums[-1]:
                right = mid - 1
            else:
                left = mid + 1
        return nums[left]



class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right)//2
            if nums[mid] < nums[-1]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
