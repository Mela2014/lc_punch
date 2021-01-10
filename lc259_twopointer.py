class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        rslt = 0
        for left, num in enumerate(nums[:-2]):
            if num*3 >= target:
                return rslt
            mid, right = left+1, len(nums)-1
            while mid < right:
                if nums[mid]+nums[right]+num < target:
                    rslt += right-mid
                    mid += 1
                else:
                    right -= 1
        return rslt
