class Solution:
    def largestNumber(self, nums):
        self.quickSort(nums, 0, len(nums)-1)
        return str(int("".join(map(str, nums))))

    def quickSort(self, nums, l, r):
        if l >= r: return
        pos = self.partition(nums, l, r)
        self.quickSort(nums, l, pos-1)
        self.quickSort(nums, pos+1, r)

    def partition(self, nums, l, r):
        pivot = l
        while l < r:
            if str(nums[l]) + str(nums[r]) > str(nums[r]) + str(nums[l]) :
                nums[l], nums[pivot] = nums[pivot], nums[l]
                pivot += 1
            l += 1
        nums[pivot], nums[r] = nums[r], nums[pivot]
        return pivot
