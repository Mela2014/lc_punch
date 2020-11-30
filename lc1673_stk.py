class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stk, tl= [], len(nums)
        for i, num in enumerate(nums):
            while stk and stk[-1] > num and tl-i+len(stk) > k:
                stk.pop()
            stk.append(num)
        return stk[:k]
