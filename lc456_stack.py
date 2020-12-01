class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stk, last = [], -float("inf")
        for num in nums[::-1]:
            # last is ensured to be less than one seen item
            if num < last:
                return True
            # mono-decreasing-stack maintaining value for nums[k] aka last
            while stk and stk[-1] < num:
                last = stk.pop()
            stk.append(num)
        return False
