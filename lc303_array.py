class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.nums = [0]*(n+1)
        for i in range(n):
            self.nums[i+1] = self.nums[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right+1]-self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
